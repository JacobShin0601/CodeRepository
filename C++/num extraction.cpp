#include <iostream>
#include <stdio.h>

using namespace std;

int main(int argc, char *argv[]) {
	freopen("input.txt", "rf", stdin);
	
	char input_source[50];
	int i, j, count, extracted_number;
	
	scanf("%s", input_source);

//	cout << extracted_number[0] << endl;
	
	/// test input is 028
	for (i=0; input_source[i]!='\0'; ++i){
		if(48<=input_source[i] && input_source[i]<=57){ // to extract numbers
			extracted_number = extracted_number*10 + (input_source[i]-48); // MEMORIZE IT!
		}// if - extract numbers & calculation
	} // for loop - search input source one by one
	
	cout << extracted_number << endl;
	
	
	// calculation of submultiple
	int count_submultiple = 0;
	for (j=1; j<=extracted_number; j++){
		if(extracted_number%j==0){
			cout << j << " ";
			count_submultiple++;
		}
	}
	cout << endl;
	cout << count_submultiple << endl;
	
}// end of main