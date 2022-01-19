#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	freopen("input.txt", "rt", stdin);
	int num_A, num_B, p1=0, p2=0, p3=0;
	scanf("%d", &num_A);
	vector<int> A(num_A);
	for(int i=0; i<num_A; i++){
		scanf("%d", &A[i]);
	}
	sort(A.begin(), A.end());
	
	scanf("%d", &num_B);
	vector<int> B(num_B);
	for(int i=0; i<num_B; i++){
		scanf("%d", &B[i]);
	}
	sort(B.begin(), B.end());
	
	vector<int> join;
	
	while(p1<num_A && p2<num_B){
		if(A[p1]==B[p2]){
			join.push_back(A[p1++]);
			p2++;p3++;
		}
		else if(A[p1]<B[p2]){
			p1++;
		}
		else{p2++;}
	}
	for (int i:join){
		cout << i << " ";
	}
	return 0;
}