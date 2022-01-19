#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	#include <iostream>
	#include <stdio.h>
	
	using namespace std;
	
	cout << "Enter 'n', will return all the number of submultiple by n" << endl;
	int n;
	cin >> n;
	
	int i, j;
	for (i=1; i<=n; i++){
		int cnt = 0;
		
		for (j=1; j<=i; j++){
			if (i%j==0) {cnt++;}
		}
		
		if(cnt==2){cout << i << " ";}
	}
	cout << endl;
	cout << "end of program...";
	
	return 0;
}

