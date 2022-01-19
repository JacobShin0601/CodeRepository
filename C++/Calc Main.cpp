#include "Calc header.h"

int main() {
	Calc st1(10);
	st1.add(10).sub(2).mult(3).print();
	
	Calc(10).add(10).sub(2).mult(3).print();
}