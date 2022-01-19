#include <iostream>
#include <limits>

using namespace std;
int main(int argc, char *argv[]) {
//	cout << char (65) << endl;
//	cout << int('A') << endl;
//	
//	cout << static_cast<char> (65) << endl;
//	cout << static_cast<char> ('A') << endl;
//	
	
	char c1(65);
	
//	cin >> c1;
//	cout << c1 << " " << static_cast<int> (c1) << endl;
//	
//	cin >> c1;
//	cout << c1 << " " << static_cast<int> (c1) << endl;
//	
//	cin >> c1;
//	cout << c1 << " " << static_cast<int> (c1) << endl;
	
	cout << sizeof(unsigned char) << endl;
	cout << (int)std::numeric_limits<unsigned char>::max() << endl;
	cout << (int)std::numeric_limits<unsigned char>::lowest() << endl;
}