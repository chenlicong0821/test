#include <iostream>
#include <stdlib.h>
#include <stdint.h>

using namespace std;

int main(int argc, char **argv)
{
    const char *str = "1553803200.433";
    double f = atof(str);
    int64_t l = f*1000;

    cout << str << endl;
    cout << f << endl;
    cout << l << endl;

    return 0;
}

