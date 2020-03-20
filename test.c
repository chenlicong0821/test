#include <stdio.h>
#include <stdlib.h>

void test1()
{
    int count = 0;
    int i = 0;
    for (; i < 10; i++)
    {
        count = count++;
    }

    printf("%d\n", count);
}

#pragma pack(2)
struct AA
{
    int a;
    char b;
    short c;
    char d;
} a;
#pragma pack()

void test2 ()
{
    printf("%d\n", sizeof(a));
}

int main(int argc, char **argv)
{
    test2();

    return 0;
}
