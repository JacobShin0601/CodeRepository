#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	freopen("input.txt", "rt", stdin);
	int num_input=0;
	scanf("%d", &num_input);
	
	std::vector<int> grade_vector(num_input);
	std::vector<int> ranking_vector(num_input);
	
	for (int i=0; i<num_input; i++){
		int temp=0;
		scanf("%d", &temp);
		grade_vector[i] = temp;
		ranking_vector[i] = 1;
	}
	
	for (int i=0; i<num_input; i++){
		
		for (int j=0; j<num_input; j++){
			if(grade_vector[i]<grade_vector[j]){
				ranking_vector[i] = ranking_vector[i] + 1;
			}
		}
	}
	for (int i=0; i<num_input; i++){
		cout << ranking_vector[i] << " ";
	}
	return 0;
}