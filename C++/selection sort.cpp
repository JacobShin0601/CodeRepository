#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	freopen("input.txt", "rt", stdin);
	
	int num_int;
	scanf("%d", &num_int);
	
	std::vector<int> unsorted_vector(100);
	std::vector<int> sorted_vector(100);
	
	for (int i=0; i<num_int; i++){
		int temp;
		scanf("%d", &temp);
		unsorted_vector[i] = temp;
	}
	
	for (int i=0; i<(num_int); i++){
		
		for (int j=i+1; j<num_int; j++){
			if (unsorted_vector[i]>unsorted_vector[j]){
				int temp;
				temp = unsorted_vector[i];
				unsorted_vector[i] = unsorted_vector[j];
				unsorted_vector[j] = temp;
			}
		}
		sorted_vector[i] = unsorted_vector[i];
	}
	
	for (int i=0; i<num_int; i++){
		cout << sorted_vector[i] << " ";
	}
	
	return 0;
}