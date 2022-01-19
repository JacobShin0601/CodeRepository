#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	int x = 5;
	int *ptr_x = &x, *ptr_y = &x;
	
	cout << typeid(ptr_x).name() << endl;
	
	return 0;
//	cout << ptr_x << endl;
//	cout << *ptr_y << endl;
}