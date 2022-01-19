#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

int digit_sum(int x){
	int tmp, sum = 0;
	
	while (x>0){
		tmp = x%10; // digit on the last position (under 10)
		sum += tmp;
		x = x/10;
	}
	return sum;
}

int main(int argc, char *argv[]) {
	freopen("input.txt", "rf", stdin);
	
	int i, n, input_num, temp_sum, result_value;
	int max_sum = -2147000000;
//	std::vector<int> my_vector;
	
	scanf("%d", &n);
	
	for (i=0; i<n; i++){
		scanf("%d", &input_num);
		temp_sum = digit_sum(input_num);
		
		if(max_sum<temp_sum){max_sum=temp_sum; result_value = input_num;}
		else if (temp_sum == max_sum) {
			if (input_num > result_value) {result_value = input_num;}
		}
	} // for loop : single component search and make digit_sum -> comparison with max value
	
	cout << result_value << endl;
	return 0;
}