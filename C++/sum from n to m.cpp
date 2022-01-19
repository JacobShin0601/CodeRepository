#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	int n, m, i;
	cin >> n >> m;
	
//	cout << n << " " << m << endl;
	
	int sum = 0;
	
	for (i = n; i <= m; i++){

		sum += i;
		
		cout << i;
		if(i!=m){
			cout<<" + ";
		}//if
	}//for
	
	cout << " = " << sum << endl;
}//main