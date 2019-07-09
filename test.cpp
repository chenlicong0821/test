#include <iostream>
#include <typeinfo>

using namespace std;

int main(int argc,char *argv[])
{
    cout << typeid(1.0).name() << endl;
    cout << typeid(1/2).name() << endl;
    cout << typeid(2.0/3).name() << endl;

    return 0;
}
