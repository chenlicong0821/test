#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <sys/socket.h>
#include <sys/epoll.h>
#include <arpa/inet.h>
#include <fcntl.h>

#define MAX_EVENT_NUM           1024
#define BUFFER_SIZE             10
#define true                    1
#define false                   0

int setnonblocking(int fd)
{
    int old_opt = fcntl(fd, F_GETFD);
    int new_opt = old_opt | O_NONBLOCK;
    fcntl(fd, F_SETFD, new_opt);

    return old_opt;
}//将文件描述符设置为非阻塞的

void addfd(int epollfd, int fd, int enable_et)
{
    struct epoll_event event;
    event.data.fd = fd;
    event.events = EPOLLIN;
    if(enable_et){
            event.events |= EPOLLET;
    }
    epoll_ctl(epollfd, EPOLL_CTL_ADD, fd, &event);
//    setnonblocking(fd);
}//将文件描述符fd的EPOLLIN注册到epollfd指示的epoll内核事件表中，enable_et表示是否对fd启用ET模式

void lt(struct epoll_event *events, int num, int epollfd, int listenfd)
{
    char buf[BUFFER_SIZE];
    for(int i = 0; i < num; i++){
            int sockfd = events[i].data.fd;
            if(sockfd == listenfd){
                    struct sockaddr_in clientaddr;
                    socklen_t clilen = sizeof(clientaddr);
                    int connfd = accept(listenfd, (struct sockaddr *)&clientaddr, &clilen);
                    addfd(epollfd, connfd, false);//对connfd使用默认的lt模式
            }else if(events[i].events & EPOLLIN){//只要socket读缓存中还有未读的数据，这段代码就会触发
                    printf("event trigger once\n");
                    memset(buf, '\0', BUFFER_SIZE);
                    int ret = recv(sockfd, buf, BUFFER_SIZE-1, 0);
                    if(ret <= 0){
                            close(sockfd);
                            continue;
                    }
                    printf("get %d bytes of content:%s\n", ret, buf);
            }else{
                    printf("something else happened\n");
            }
    }
}

void et(struct epoll_event *event, int num, int epollfd, int listenfd)
{
    char buf[BUFFER_SIZE];
    for(int i = 0; i < num; i++){
            int sockfd = event[i].data.fd;
            if(sockfd == listenfd){
                    struct sockaddr_in clientaddr;
                    socklen_t clilen = sizeof(clientaddr);
                    int connfd = accept(listenfd, (struct sockaddr *)&clientaddr, &clilen);
                    addfd(epollfd, connfd, true);//多connfd开启ET模式
            }else if(event[i].events & EPOLLIN){
                    printf("event trigger once\n");
                    while(1){//这段代码不会重复触发，所以要循环读取数据
                            memset(buf, '\0', BUFFER_SIZE);
                            int ret = recv(sockfd, buf, BUFFER_SIZE-1, 0);
                            if(ret < 0){
                                    if((errno == EAGAIN) || (errno == EWOULDBLOCK)){
                                            printf("read later\n");
                                            break;
                                    }
                                    close(sockfd);
                                    break;
                            }else if(ret == 0){
                                    close(sockfd);
                            }else{
                                    printf("get %d bytes of content:%s\n", ret, buf);
                            }
                    }
            }else{

                    printf("something else happened \n");
            }
    }
}

int start_ser(char *ipaddr, char *port)
{
        int sock = socket(AF_INET, SOCK_STREAM, 0);

        struct sockaddr_in serveraddr;
        bzero(&serveraddr, sizeof(serveraddr));
        serveraddr.sin_family = AF_INET;
        serveraddr.sin_port = htons(atoi(port));
        inet_pton(AF_INET, ipaddr, &serveraddr.sin_addr);

        bind(sock, (struct sockaddr *)&serveraddr, sizeof(serveraddr));

        listen(sock, 128);

        return sock;
}

int main(int argc, char *argv[])
{
        int listenfd = start_ser(argv[1], argv[2]);

        struct epoll_event events[MAX_EVENT_NUM];
        int epollfd = epoll_create(5);
        if(epollfd < 0){
                printf("epoll_create err");
        }
        addfd(epollfd, listenfd, true);
        while(1){
                int ret = epoll_wait(epollfd, events, MAX_EVENT_NUM, -1);
                if(ret < 0){
                        printf("epoll failure\n");
                        break;
                }

                //lt(events, ret, epollfd, listenfd);//lt模式
                et(events, ret, epollfd, listenfd);//et模式
        }
        close(listenfd);
        return 0;
}
