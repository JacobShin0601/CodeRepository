#include <iostream>

using namespace std;

int getInt()
{
	while(true){
		cout << "Enter a integer number : ";
		int x;
		cin >> x;
		
		if (std::cin.fail())
			{
				std::cin.clear();
				std::cin.ignore(32767, '\n');
				cout << "Invalid number, please type in again" << endl;
			}
		else {
			std::cin.ignore(32767, '\n');
			return x;
		}
	}
}

char getOperator()
{
	while(true)
		{
			cout << "Enter an operator (+, -) : ";
			char op;
			cin >> op;
			
			if(op=='+' | op == '-'){return op;}
			else {cout << "Invalid operator, please type in again" << endl;}
		}
}

void printResult(int x, char op, int y)
{
	switch (op) {
		case '+':
			cout << x+y << endl;
			break;
		case '-':
			if(x>y) {cout << x-y << endl;}
			else {cout << y-x << endl;}
			break;
//		default: 
//			{cout << "Invalid operator" << endl;}
	}
}

int main(int argc, char *argv[]) {

printResult(getInt(), getOperator(), getInt());
	
}