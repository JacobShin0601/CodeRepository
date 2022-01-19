#include <iostream>

using namespace std;
int main(int argc, char *argv[]) {
	
	int num_people = 0;

	freopen("input.txt", "rf", stdin);
	scanf("%d", &num_people);
	
	int sit_height[num_people];
	for (int i=0; i<num_people; i++){
		scanf("%d", &sit_height[i]);
	}
	
	//Comparison
	int cnt = 0;
	
	for (int i = 0; i<num_people-1; i++){
		int max = sit_height[i];
		for (int j = i+1; j<num_people; j++){
			if(sit_height[i]<sit_height[j]) {max=sit_height[j]; break;}
			else {continue;}
			}
		if(max == sit_height[i]){
			cnt++;
		}
	}
	cout << cnt << endl;
}