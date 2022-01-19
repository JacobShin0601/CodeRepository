#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	int input=0;
	cin >> input;
	
	vector<int> prime_factor(input+1); // to include itself as prime factor
	
	for (int i=2; i<=input; i++){
		int temp=i;
		int j=2;
		
		while(1){
			if(temp%j==0){
				prime_factor[j]++;
				temp = temp/j;
			}
			else {j++;}
			
			if(temp==1) {break;}
		}
	}
	
	cout << input << "! = ";
	for (int i=2; i<=input; i++){
		if(prime_factor[i]!=0){
			cout << prime_factor[i] << " ";
		}
	}
	return 0;
}