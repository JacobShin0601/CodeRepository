#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	freopen("input.txt", "rt", stdin);
	int num_score;
	scanf("%d", &num_score);
	std::vector<int> score_vector(100);
	
	for(int i=0; i<num_score; i++){
		int temp;
		scanf("%d", &temp);
		score_vector[i]=temp;
	}
	
	for(int i=0; i<num_score-1; i++){
		int idx_largest_num=0;
		for(int j=i+1; j<num_score; j++){
			if(score_vector[i]<score_vector[j]){
				int temp = score_vector[j];
				score_vector[j] = score_vector[i];
				score_vector[i] = temp;
			}
		}
	}
	
	int cnt=0;	
	for(int i=0; i<num_score; i++){
		if(score_vector[i]!=score_vector[i+1]){
			cnt++;
		}
		if(cnt==2){
			cout << score_vector[i+1];
			break;
		}
	}
	
	//cout << score_vector[2] << endl;
}