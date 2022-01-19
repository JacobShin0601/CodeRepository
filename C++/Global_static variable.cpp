#include <iostream>

using namespace std;

//int a = 1;

void doSomething()
{
	int a = 1;
	++a;
	cout << a << endl;
	cout << &a << endl;
}


int main() {
	doSomething();
	doSomething();
	doSomething();
	doSomething();
}