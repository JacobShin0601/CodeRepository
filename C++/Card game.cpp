#include <iostream>

using namespace std;
int main(int argc, char *argv[]) {
	
	freopen("input.txt", "rt", stdin);
	int A_card[9];
	int B_card[9];
	
	//distribute 10 card each to player
	for(int i=0; i<10; i++){
		scanf("%d", &A_card[i]);
	}
	for(int i=0; i<10; i++){
		scanf("%d", &B_card[i]);
	}
	
	//compare cards, give scores accordingly
	int score_A=0;
	int score_B=0;
	for(int i=0; i<10; i++){
		if(A_card[i]>B_card[i]){
			score_A += 3;
		}
		else if(A_card[i]<B_card[i]){
			score_B += 3;
		}
		else if(A_card[i]==B_card[i]){
			score_A += 1;
			score_B += 1;
		}
	}
	
	cout << score_A << " " << score_B << endl;
	
	if(score_A>score_B){cout << "A" << endl;}
	else if(score_A<score_B){cout << "B" <<endl;}
	else if(score_A==score_B){
		for(int i=9; i>=0; i--){
			if(A_card[i]==B_card[i]){continue;}
			else if(A_card[i]>B_card[i]){cout << "A" << endl;break;}
			else if(A_card[i]<B_card[i]){cout << "B" << endl;break;}
		}
	}
	
}