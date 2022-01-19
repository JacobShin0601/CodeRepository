#include <iostream>
#include <vector>

using namespace std;
int main(int argc, char *argv[]) {
	int input;
	cin >> input;
	
	int n_factorial=1;
	for (int i=2; i<=input; i++){
		n_factorial=n_factorial*i;
	}
	
	std::vector<int> elements;
	int element;
	int temp = n_factorial;
	
	for (int i=0; i<input; i++){
		element = temp%10;
		elements.push_back(element);
		temp=temp/10;
	}
	
	int cnt=0;
	int max=0;
	for (int i=0; i<input; i++){
		if(elements[i]==0){
			cnt++;
			if(max<cnt){max=cnt;}
			else {
				cnt=0;
			}
		}
	}
	cout << max << endl;
	return 0;
}