#include <iostream>

using namespace std;

class Fraction {
public:
	int _numerator;
	int _denominator;

public:
	Fraction(const int& numerator_input=1, const int denominator_input=1){
		_numerator = numerator_input;
		_denominator = denominator_input;
	}
	void print () {
		cout << _numerator << "/" << _denominator << endl;
	}
};	

int main(int argc, char *argv[]) {
	
//	Fraction frac(1, 2);
//	frac.print();
	
	Fraction one_thirds(1, 3);
	one_thirds.print();
}