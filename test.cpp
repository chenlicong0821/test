#include <stdio.h>
#include <string.h>
#include <iostream>

#define CODE_LEN    16

using namespace std;

int main(int argc,char *argv[])
{
    const char *pSymbol = "BABA";
    char logSymbol[CODE_LEN];

    if (pSymbol != NULL && strlen(pSymbol) >= 1)
    {
        snprintf(logSymbol, CODE_LEN, ",%s", pSymbol);
    }
    else
    {
        snprintf(logSymbol, CODE_LEN, "");
    }

    printf("1%s2\n", logSymbol);

    cout << "1" << logSymbol << "2" << endl;

    return 0;
}
