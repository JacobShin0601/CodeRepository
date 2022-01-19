#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	const int value = 5;
	const int *ptr = &value;


	int value2 = 10;
	ptr = &value2;
	
	cout << *ptr << endl;
}