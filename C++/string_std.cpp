#include <iostream>
#include <string>
#include <limits>

using namespace std;
int main(int argc, char *argv[]) {
//	const string my_hello = "Hello, world";
//	
//	string my_ID = "123";
//	
//	cout << my_hello << endl;
////	cout << my_ID << endl;
//	
//	cout << "Your age? ";
//	int age;
//	cin >> age;
//	//	cin >> age;
//	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
//	
//	cout << "Your name? ";
//	string name;
//	std::getline(std::cin, name);
////	cin >> name;
//	
////	cout << "Your age? ";
////	int age;
////	cin >> age;
//	
//	cout << name << " " << age << endl;
	
	
	string a("Jacob");
	string b("32");
	string hw = a+" "+b;
	hw += " He's good";
	
	cout << hw << endl;
	cout << hw.length() << endl;
	
	return 0;
}