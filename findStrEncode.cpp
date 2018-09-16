#include <stdio.h>
#include <string.h>

/*
bb 2015/6/15 19:11:45
1、a[n]为n个互不相同的整数组成的数组,要求输出同时满足下面两个条件的整数，要求时间复杂度O(n)，不能用递归
（1）比前面所有的整数都大
（2）比后面所有的整数都小
*/
int findN0(int *arr, int n)
{
    if (arr == NULL) return 0;

    int *arr2 = new int[n];
    int id = 0;
    arr2[id++] = arr[0];

    int max = arr[0];
    int i;

    for (i = 1; i < n; i++)
    {
        if (arr[i] > max)
        {
            arr2[id++] = arr[i];
            max = arr[i];
        }
        else
        {
            while (id>0 && arr2[id-1] >= arr[i])
            {
                id--;
            }
        }

    }

    for (i = 0; i<id; i++)
        printf("%d ", arr2[i]);
    printf("\n");

    delete []arr2;
    return id;
}

/*
2、c语言编码：不借助其他库，在c语言里，将一个正整数转化为对应的二进制字符串
*/
void int2str(unsigned int a, char *str)
{
    unsigned int num = a;
    char *newStr = str;
    int i = 0, j = 0;
    char temp;
    do
    {
        *newStr++ = num%10 + '0';
        num /= 10;
        i++;
    } while(num);
    *newStr = '\0';
    printf("str:%s,len:%d\n", str, strlen(str));

    int mid = i/2;
    i--;
    while (i>=mid && j<mid)
    {
        temp = str[j];
        str[j] = str[i];
        str[i] = temp;
        j++;
        i--;
    }
    printf("str:%s,len:%d\n", str, strlen(str));
}


/*
3、c语言编码：我现在有一段明文和它对应的TEA对称密钥算法加密后的密文，但我不知道密钥是什么。
已知TEA对称密钥加密算法的密钥是128 bits的，我希望遍历所有密钥的可能值，尝试对这段明文加密后是否等于密文，
来达到找出密钥的目的（暴力破解）。请写出遍历所有密钥的可能值的代码。不能用递归
*/
char g_sMing[] =  "a0c";
char g_sMiwen[] = "b8d";
char g_sEncode[4] = {0};
char *encode(char *strMing, unsigned long long arrMiyue[])
{
    char *strEncode = g_sEncode;
    char *sMing = strMing;
    unsigned long long arrMiyue2[2] = {0};
    int bytes = sizeof(unsigned long long);
    if (strlen(strMing) < bytes)
    {
        bytes = strlen(strMing);
    }
    for (int i = 0; i < 1; i++)
    {
        arrMiyue2[i] = arrMiyue[i];
        for (int j = 0; j < bytes; j++)
        {
            *strEncode++ = (arrMiyue2[i] & 0xFF) + *sMing++;
            arrMiyue2[i] = arrMiyue2[i] >> 8;
        }
    }

    return g_sEncode;
}

#define MAXLONGLONG 0xFFFFFF
int deKey()
{
    char *strMing = g_sMing;
    char *strMiwen = g_sMiwen;
    unsigned long long arrMiyue[2] = {0};
    while (arrMiyue[0] != MAXLONGLONG)
    {
        char *strEncode = encode(strMing, arrMiyue);
        // printf("%s\n", strMing);
        // printf("%02x %02x\n", arrMiyue[0], arrMiyue[1]);
        // printf("%s\n", strEncode);
        // printf("%s\n", strMiwen);
        if (strcmp(strEncode, strMiwen) == 0)
        {
            printf("%llu %llu\n", arrMiyue[0], arrMiyue[1]);
            char *strMiyue = (char *)arrMiyue;
            for (int i = 0; i < 16; i++)
            {
                printf("%02x ", strMiyue[i]);
            }
            printf("\n");
        }

        // 简单测试，arrMiyue[1]不处理
        // if ( arrMiyue[0] == MAXLONGLONG)
        // {
        //     arrMiyue[1]++;
        // }
        arrMiyue[0]++;
    }
    // printf("%02x %02x\n", arrMiyue[0], arrMiyue[1]);
}

int main()
{
    printf("%d,%d,%d,%d\n\n", sizeof(int), sizeof(long), sizeof(long long), sizeof(unsigned long long));

    int arr[10] = {1, 3, 2, 4, 6, 5, 7, 9, 8, 10};
    int n = sizeof(arr)/sizeof(arr[0]);
    printf("n:%d\n", n);
    int id = findN0(arr, n);
    printf("id:%d\n\n", id);

    int a = 12345678;
    char s[9];
    int2str(a, s);
    printf("s:%s\n\n", s);

    deKey();

    return 0;
}
