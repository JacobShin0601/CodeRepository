#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

template <typename T>
std::string ToSting (T x){
	std::ostringstream osstream;
	osstream << x;
	return osstream.str();
	
}

int main(int argc, char *argv[]) {
//	{
//		char *strHello = new char[7];
//		strcpy(strHello, "Hello!");
//		cout << strHello << endl;
//	}
	
	{
		std::string string;
		std::wstring wstring;
		
		wchar_t wc;
		
		std::locale::global(std::locale(""));
		std::wcout.imbue(std::locale());
		
	}
	
	std::string my_string (to_string(1004));
	cout << my_string << endl;
	
	std::string my_string2 (to_string(128));
	cout << my_string+my_string2 << endl;
	
	int i = std::stoi(my_string)
	
	
}