#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char **argv)
{
    char *str = "1553803200.433";
    double f = atof(str);
    int64_t l = f*1000;

    printf("%s,%f,%ld\n", str, f, l);

    return 0;
}
