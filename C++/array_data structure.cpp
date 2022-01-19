#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	int values[10] = {2, 3, 5, 7, 11, 13, 15, 17, 21, 23};
	
	cout << sizeof(int) << endl;
	
	int offset = (long)&(values[2]) - (long)&(values[0]);
	cout << offset << endl;
}