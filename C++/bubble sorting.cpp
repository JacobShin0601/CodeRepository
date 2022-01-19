#include <iostream>

using namespace std;

void printArray(const int array[], int length){
	for(int i = 0; i < length; ++i){
		cout << array[i] << " ";
	}
	cout << endl;
}

int main(int argc, char *argv[]) {
	
	const int length = 7;
	int array[length] = {7, 2, 4, 6, 1, 5, 3};
	
	//initial status declaralation
	printArray(array, length);
	
	//Swapping method
	for(int startIndex = 0; startIndex < length-1; ++startIndex){
		
		for(int comparingIndex1 = 0; comparingIndex1 < length-1; ++comparingIndex1){
			
			int comparingIndex2 = comparingIndex1+1;
			
			if(array[comparingIndex1]>array[comparingIndex2]){
				int temp = array[comparingIndex1];
				array[comparingIndex1] = array[comparingIndex2];
				array[comparingIndex2] = temp;
			}
			
		}
		printArray(array, length);
	}	
}