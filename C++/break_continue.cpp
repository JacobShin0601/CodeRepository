#include <iostream>

using namespace std;

void breakOrReturn()
{
	while(true)
		{
			char ch;
			cin >> ch;
			
			if(ch == 'b')
				break;
			if(ch == 'r')
				return;
		}
	
	cout << "Hello" << endl;
}


int main(int argc, char *argv[]) {
	
int count(0);

while(true)
{
	char ch;
	cin >> ch;
	
	if(ch=='x'){
		cout << "What I expected was " << ch << endl;
		break;
	}
	else {
		cout << "This is not what I expected" << endl;
	}
}
	cout << "Successfully finished" << endl;
	
}