#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	freopen("input.txt", "rt", stdin);
	int num_input;
	scanf("%d", &num_input);
	
	std::vector<int> input_vector(num_input);
	for(int i=0; i<num_input; i++){
		int temp;
		scanf("%d", &temp);
		input_vector[i]=temp;
	}
	
	std::vector<int> sorted_input(num_input);
	for(int i=0; i<num_input-1; i++){
		for (int j=0; j<num_input-i-1; j++){
			if(input_vector[j]>input_vector[j+1]){
				int temp;
				temp = input_vector[j+1];
				input_vector[j+1] = input_vector[j];
				input_vector[j] = temp;
			}
		}
	}
	
	for(int i=0; i<num_input; i++){
		cout << input_vector[i] << " ";
	}
}