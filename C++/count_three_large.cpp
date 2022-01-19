#include <iostream>

using namespace std;
int main(int argc, char *argv[]) {
	int n, lt=1, cur, rt, k=1, cumulated_sum=0; //k는 자리수
	freopen("input.txt", "rt", stdin);
	scanf("%d", &n);
	
	while(lt!=0){//5367의 경우
		lt=n/(k*10); // 536 -> 53
		cur=(n/k)%10; // 7 -> 6
		rt = n%k; // 0 -> 7
		
		if(cur>3){
			cumulated_sum = cumulated_sum + ((lt+1)*k);
		}
		else if(cur<3){
			cumulated_sum = cumulated_sum + (lt*k);
		}
		else{
			cumulated_sum = cumulated_sum + (lt*k+(rt+1));
		}
		
		k=k*10;
	}
	
	cout << cumulated_sum << endl;
	return 0;
}