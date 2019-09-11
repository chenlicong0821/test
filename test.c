#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int count = 0;
    int i = 0;
    for (; i < 10; i++)
    {
        count = count++;
    }

    printf("%d\n", count);

    return 0;
}
