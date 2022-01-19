#include <iostream>

using namespace std;

void isEvenNumber(int a){
	if (a % 2==0){
		cout << "Input is even number!"<<endl;
	}
	else {
		cout << "Input is odd number!" << endl;
	}
}


int main(int argc, char *argv[]) {
	int x;
	cin >> x;
	isEvenNumber(x);
	return 0;
}