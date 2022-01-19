#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	freopen("input.txt", "rt", stdin);
	int num_input;
	scanf("%d", &num_input);
	
	vector<int> input_vector(num_input);
	for(int i=0; i<num_input; i++){
		int temp;
		scanf("%d", &temp);
		input_vector[i]=temp;
	}
	
	int i, j;
	//doing insertion sort
	for(i=1; i<num_input; i++){
		int temp = input_vector[i];
		for(j=i-1; j>=0; j--){
			if(temp < input_vector[j]){
				input_vector[j+1] = input_vector[j];
			}
			else {break;}
//			input_vector[j+1] = temp;
		}
		input_vector[j+1] = temp;
	}
	
	for(int i=0; i<num_input; i++){
		cout << input_vector[i] << " ";
	}
	
	return 0;
}