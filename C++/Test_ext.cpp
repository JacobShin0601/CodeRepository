#include <iostream>

using namespace std;

extern void doSomething();
extern int a;

int main(int argc, char *argv[]) {
//	int a = 10;
	doSomething();
	cout << a << endl;
}

////////////////////////////////////
int a = 123;

void doSomething()
{
	using namespace std;
}