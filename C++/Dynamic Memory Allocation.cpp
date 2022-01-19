#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	
	int *ptr = new (std::nothrow)int {7};
	
	cout << &ptr << endl;
	cout << ptr << endl;
	cout << *ptr << endl;
	
	delete ptr;
	
	cout << "After delete" << endl;
	if(ptr != nullptr){
		cout << ptr << endl;
		cout << *ptr << endl;
	}
	
}