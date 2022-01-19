#include <iostream>

using namespace std;

void foo (int *ptr){
	cout << *ptr << "  " << ptr << "  " << &ptr << endl;
}

int main(int argc, char *argv[]) {
	int value = 5;
	
	cout << value << " " << &value << endl;
	
	int *ptr = &value;
	foo(ptr);
	foo(&value);
//	foo(5);
	
	return 0;

}