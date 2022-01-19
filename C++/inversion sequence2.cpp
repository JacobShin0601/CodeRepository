#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	//making and distribute inputs to variables
	freopen("input.txt", "rt", stdin);
	int num_element;
	scanf("%d", &num_element);
	std::vector<int> inversion_sequence(num_element);
	std::vector<int> original_sequence(num_element);
	
	for(int i=0; i<num_element; i++){
		int temp;
		scanf("%d", &temp);
		inversion_sequence[i]=temp;
		original_sequence[i]=-1;
	}

	for(int i=num_element-1; i>=0; i--){
		int num_move = inversion_sequence[i];
		for (int j=i; j<=i+num_move; j++){
			original_sequence[j] = original_sequence[j+1];
		}
		original_sequence[i+num_move] = i+1;
	}
	
	for(int i=0; i<num_element; i++){
		cout << original_sequence[i] << " ";
	}
}