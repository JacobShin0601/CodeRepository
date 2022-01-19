#include <iostream>
#include <regex>

using namespace std;

int main(int argc, char *argv[]) {
	string str5 = "number list : 1234, 5678, 9101112";
	regex reg5("[0-9]");	//	regex reg5(R"(\d)");
	sregex_iterator it(str5.begin(), str5.end(), reg5);
	sregex_iterator it_end;
	
	while(it != it_end){
		smatch tmp = *it;
		cout << tmp.str() << " ";
		++it;
	}

}