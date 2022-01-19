#include <iostream>
#include <stack>

using namespace std;

int main(int argc, char *argv[]) {
	std::stack<std::string> s;
	
	s.push("Orange"); s.push("Blue"); s.push("Illinois");
	
	cout << "First pop(): " << s.top() << endl;
	s.pop();
	
	s.push("Illini");
	cout << "Second pop(): " << s.top() << endl;
	
	return 0;

}