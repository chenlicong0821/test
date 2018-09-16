#include <iostream>
using namespace std;

class Fraction
{
public:
    explicit Fraction(int num, int den=1)
        :m_numerator(num), m_denominator(den)
    {
        cout << "explicit Fraction(" << num << ", " << den << ")" << endl;
        cout << "m_numerator:" << m_numerator << ", m_denominator:" << m_denominator << endl;
    }

    operator double() const
    {
        cout << "double(), m_numerator:" << m_numerator << ", m_denominator:" << m_denominator << endl;
        return (double)m_numerator / m_denominator;
    }

    // Fraction operator+(const Fraction& f)
    // {
    //    cout << "operator+(): " << m_numerator << '/' << m_denominator << " + "
    //     << f.m_numerator << '/' << f.m_denominator <<  endl;
    //    return f;
    // }

    Fraction(double d)
        :m_numerator(d * 1000), m_denominator(1000)
    {
        cout << "Fraction(" << d << ")" << endl;
        cout << "m_numerator:" << m_numerator << ", m_denominator:" << m_denominator << endl;
    }


private:
    int m_numerator;
    int m_denominator;
};

int main()
{
    Fraction f(3, 5);
    double d = 4 + f;
    cout << "d:" << d << endl;
    Fraction e = f + 5;
    cout << "e:" << e << endl;
    int a = f + 6;
    cout << "a:" << a << endl;

    return 0;
}
