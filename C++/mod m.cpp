#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	int n, m, i, sum = 0;
	cin >> n >> m;
	
	for (i=1; i<=n; i++){
		if(i%m==0){
			sum += i;
		}//if
	}//for
	cout << sum << endl;
}//main
