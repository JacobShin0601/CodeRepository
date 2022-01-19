#include <iostream>

using namespace std;
int main(int argc, char *argv[]) {
	constexpr int my_const(123);
	
	int number;
	cin >> number;
	
	const int special_number(number);
	cout << number << endl;
}