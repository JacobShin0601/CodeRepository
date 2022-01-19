#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	int i, j, cnt=0, input = 0;
	
	freopen("input.txt", "rf", stdin);
	scanf("%d", &input);
	
	for(i=2; i<=input; i++){
		bool flag = true;
		for(j=2; j<i; j++){
			if(i%j==0){flag=false;}
		}
		if(flag==true){cnt++;}
	}
	
	cout << cnt << endl;
}