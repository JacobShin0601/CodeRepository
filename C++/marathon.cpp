#include <iostream>
#include <vector>

using namespace std;
int main(int argc, char *argv[]) {
	freopen("input.txt", "rt", stdin);
	
	int num_people;
	scanf("%d", &num_people);
	
	std::vector<int> performance_vector(num_people);
	std::vector<int> ranking_vector(num_people);
	for(int i=0; i<num_people; i++){
		int temp;
		scanf("%d", &temp);
		performance_vector[i]=temp;
		ranking_vector[i]=1;
	}
	
	
	for (int i=0; i<num_people; i++){
		for (int j=0; j<i; j++){
			if(performance_vector[j]>performance_vector[i]){
				ranking_vector[i]++;
			}
		}
	}
	
	for (int i=0; i<num_people; i++){
		cout << ranking_vector[i] << " ";
	}
	return 0;
}