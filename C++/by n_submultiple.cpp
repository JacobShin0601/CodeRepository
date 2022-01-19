#include <iostream>
#include <stdio.h>

using namespace std;

int main(int argc, char *argv[]) {
	cout << "Enter 'n', will return all the number of submultiple by n" << endl;
	int n;
	cin >> n;
	
	int cnt[50001];
	
	int i, j, m;
	for (i=1; i<=n; i++){
		
		for (j=i; j<=n; j=j+i){
			cnt[j]++;

		}
	}
	
//	for (m=1; m<=n; m++){
//		cout << cnt[m] << " ";
//	}
	
	cout << endl;
	cout << "end of program...";
	return 0;
}