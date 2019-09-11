#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int count = 0;
    for (int i = 0; i < 10; i++)
    {
        count = count++;
    }

    cout << count << endl;

    return 0;
}
