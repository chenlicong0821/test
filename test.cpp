#include <iostream>

using namespace std;

class Base1 {
public:
    int ibase1;
    Base1():ibase1(10) {}
    virtual void f() { cout << "Base1::f()" << endl; }
    virtual void g() { cout << "Base1::g()" << endl; }
    virtual void h() { cout << "Base1::h()" << endl; }
};

class Base2 {
public:
    int ibase2;
    Base2():ibase2(20) {}
    virtual void f() { cout << "Base2::f()" << endl; }
    virtual void g() { cout << "Base2::g()" << endl; }
    virtual void h() { cout << "Base2::h()" << endl; }
};

class Base3 {
public:
    int ibase3;
    Base3():ibase3(30) {}
    virtual void f() { cout << "Base3::f()" << endl; }
    virtual void g() { cout << "Base3::g()" << endl; }
    virtual void h() { cout << "Base3::h()" << endl; }
};

class Derive : public Base1, public Base2, public Base3 {
public:
    int iderive;
    Derive():iderive(100) {}
    virtual void f() { cout << "Derive::f()" << endl; }
    virtual void g1() { cout << "Derive::g1()" << endl; }
};

typedef void(*Fun)(void);

int main(int argc,char *argv[])
{
    Derive d;

    long** pVtab = (long**)&d;
    Fun pFun = NULL;

    cout << sizeof(Base1) << ' ' << sizeof(Base2) << ' ' << sizeof(Base3) << ' ' << sizeof(Derive) << endl;

    cout << "[0] Base1::_vptr->" << endl;
    pFun = (Fun)pVtab[0][0];
    cout << "     [0] ";
    pFun();

    pFun = (Fun)pVtab[0][1];
    cout << "     [1] ";pFun();

    pFun = (Fun)pVtab[0][2];
    cout << "     [2] ";pFun();

    pFun = (Fun)pVtab[0][3];
    cout << "     [3] "; pFun();

    pFun = (Fun)pVtab[0][4];
    cout << "     [4] "; cout<<pFun<<endl;

    cout << "[1] Base1.ibase1 = " << hex << (long)pVtab[1] << endl;

    int s = sizeof(Base1)/8;

    cout << "[" << s << "] Base2::_vptr->"<<endl;
    pFun = (Fun)pVtab[s][0];
    cout << "     [0] "; pFun();

    pFun = (Fun)pVtab[s][1];
    cout << "     [1] "; pFun();

    pFun = (Fun)pVtab[s][2];
    cout << "     [2] "; pFun();

    pFun = (Fun)pVtab[s][3];
    cout << "     [3] ";
    cout<<pFun<<endl;

    cout << "["<< s+1 <<"] Base2.ibase2 = " << hex << (long)pVtab[s+1] << endl;

    s = s + sizeof(Base2)/8;

    cout << "[" << s << "] Base3::_vptr->"<<endl;
    pFun = (Fun)pVtab[s][0];
    cout << "     [0] "; pFun();

    pFun = (Fun)pVtab[s][1];
    cout << "     [1] "; pFun();

    pFun = (Fun)pVtab[s][2];
    cout << "     [2] "; pFun();

    pFun = (Fun)pVtab[s][3];
    cout << "     [3] ";
    cout<<pFun<<endl;

    s++;
    cout << "["<< s <<"] Base3.ibase3 = " << hex << (int)(long)pVtab[s] << endl;
    cout << "["<< s <<"] Derive.iderive = " << hex << ((long)pVtab[s]>>32) << endl;

    char *p = (char *)&d;
    for (int i = 0; i < sizeof(d); ++i)
    {
        cout.width(2);
        cout << hex << (long)*(p+i) << ' ';
        if ((i+1)%8 == 0)
        {
            cout << endl;
        }
    }
    cout << endl;

    return 0;
}
