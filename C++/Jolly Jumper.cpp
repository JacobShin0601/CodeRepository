#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	
	/// input -> int and vector
	freopen("input.txt", "rt", stdin);
	
	int num_input=0;
	scanf("%d", &num_input);
	
	int element_A=0;
	int element_B=0;
	
	scanf("%d", &element_A);
	std::vector<int> input_vector(num_input);
	
	for (int i=1; i<num_input; i++){
		scanf("%d", &element_B);
		int gap_elements = abs(element_A-element_B);
		
		if (gap_elements>0 && gap_elements<num_input && input_vector[gap_elements]==0){
			input_vector[gap_elements]=1;
			element_A=element_B;
		}
		else {cout << "No" << endl; return 0;}
	}
	cout << "Yes" << endl;
	return 0;
	
//	/// comparing two elements in vector and find value in the vector
//	bool isTrue=true;
//	
//	for (int i=0; i<num_input; i++){
//		int gap_elements;
//		if(input_vector[i]<=input_vector[i+1]){
//			gap_elements = input_vector[i+1]-input_vector[i];
//		}
//		else{gap_elements = input_vector[i]-input_vector[i+1];}
//		
//		for (int j=0; j<num_input; j++){
//			if(gap_elements==input_vector[j]){break;}
//			else{isTrue=false;}
//		} 
//	}
	
}