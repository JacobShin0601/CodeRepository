#include <iostream>

using namespace std;
int main(int argc, char *argv[]) {
	
	freopen("input.txt", "rt", stdin);
	int num_game = 0;
	scanf("%d", &num_game);
	
	int A[100];
	int B[100];
	
	for (int i=0; i<num_game; i++){
		scanf("%d", &A[i]);
	}
	
	for (int j=0; j<num_game; j++){
		scanf("%d", &B[j]);
	}
	
	for (int m=0; m<num_game; m++){
		if(A[m]==B[m]){cout << "D" <<endl;}
		else if(A[m]==1&&B[m]==3){cout << "A" << endl;}
		else if(A[m]==2&&B[m]==1){cout << "A" << endl;}
		else if(A[m]==3&&B[m]==2){cout << "A" << endl;}
		else{cout << "B" << endl;}
	}
	return 0;
}