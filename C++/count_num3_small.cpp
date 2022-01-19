#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	freopen("input.txt", "rt", stdin);
	int n, temp, i, cnt=0, digit;
	scanf("%d", &n);
	
	for(i=1; i<=n; i++){
		temp = i;
		while(temp>0){
			digit=temp%10;
			if(digit==3){cnt++;}
			temp=temp/10;
		}
	}
	cout << cnt << endl;
	return 0;
}