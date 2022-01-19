#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
	int number_count[10];
	char input[100];
	int i=0, j=0;
	int temp_digit;
	
	freopen("input.txt", "rf", stdin);
	scanf("%s", input);
	
//	std::vector<int> number_count;
//	char input[100];
//	int i = 0;
	
	for (i=0; input[i]!='\0'; i++){
		temp_digit = input[i] - 48;
		number_count[temp_digit]++;
	}

	int max_temp = -2147000000;


//	auto it = max_element(std::begin(number_count), std::end(number_count));
//
	
	for (j=0; j<10; j++){
		if(max_temp<number_count[j]){
			max_temp = number_count[j];
		}
	}
	cout << max_temp << endl;
}