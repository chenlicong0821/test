
#include <iostream>
#include <vector>

using namespace std;

class Obj1
{
public:
    Obj1()
    {
        cout << "Obj1()\n";
    }
    Obj1(const Obj1 &)
    {
        cout << "Obj1(const Obj1&)\n";
    }
    Obj1(Obj1 &&)
    {
        cout << "Obj1(Obj1&&)\n";
    }
};

class Obj2
{
public:
    Obj2()
    {
        cout << "Obj2()\n";
    }
    Obj2(const Obj2 &)
    {
        cout << "Obj2(const Obj2&)\n";
    }
    Obj2(Obj2 &&) noexcept
    {
        cout << "Obj2(Obj2&&)\n";
    }
};

void test1()
{
    vector<Obj1> v1;
    v1.reserve(2);
    v1.emplace_back();
    v1.emplace_back();
    v1.emplace_back();
    v1.emplace_back();

    vector<Obj2> v2;
    v2.reserve(2);
    v2.push_back(Obj2());
    v2.push_back(Obj2());
    v2.push_back(Obj2());
    v2.emplace_back();
}

struct xx
{
    long long _x1;
    char _x2;
    int _x3;
    char _x4[2];
    static int _x5;
};
int xx::_x5;

void test2()
{
    cout << sizeof(xx) << endl;
    xx a;
    cout << &(a._x1) << endl;
    printf("%p\n", &(a._x2));
    cout << static_cast<const void *> (&(a._x2)) << endl;
    cout << &(a._x3) << endl;
    cout << &(a._x4) << endl;
    cout << &(a._x5) << endl;
}

int main()
{
    test2();
    return 0;
}
