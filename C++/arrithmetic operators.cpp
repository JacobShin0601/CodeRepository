#include <iostream>

using namespace std;
int main(int argc, char *argv[]) {
	
	int x = 7;
	int y = 4;
//	cout << std::piecewise_construct_t()
	cout << x / y << endl;
	cout << float(x) / y << endl;
	cout << x / float(y) << endl;
	cout << float(x) / float(y) << endl;
	
	cout << -5 % 2 << endl;
	
	int z = x;
	z += y;
	cout << z << endl;
	
	
	return 0;
}