#include <iostream>

using namespace std;

int pow(int base, int exponent)
{
	int result = 1;
	
	for (int count = 0; count < exponent; count++)
		{
			result *= base;
		}
	return result;
}



int main(int argc, char *argv[]) {
	
	cout << pow(2, 4) << endl;
}

