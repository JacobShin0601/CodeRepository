#include <iostream>
#include <queue>

using namespace std;

int main(int argc, char *argv[]) {
	std::queue<std::string> q;
	
	q.push("Orange"); q.push("Blue"); q.push("Illinois");
	
	cout << "First pop(): " << q.front() << endl;
	q.pop();
	
	q.push("Illini");
	cout << "Second pop(): " << q.front() << endl;
	
	return 0;
}