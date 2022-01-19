#include <iostream>

using namespace std;


class Fraction{
private:
	int m_numerator;
	int m_denominator;
	
public:
	Fraction(int num = 0, int den = 1)
	: m_numerator(num), m_denominator(den)
	{
		assert(den!=0);
	}
	
	Fraction(const Fraction& fraction)
	: m_numerator(fraction.m_numerator), m_denominator(fraction.m_denominator)
	{
		cout << "Copy constructor called" << endl;
	}
	
	friend std::ostream& operator << (std::ostream& out, const Fraction& f){
		out << f.m_numerator << " / " << f.m_denominator << endl;
		
		return out;
	}
};
int main(int argc, char *argv[]) {
	Fraction frac(3, 5);
	Fraction fr_copy(frac);
	
	cout << frac << fr_copy << endl;
}