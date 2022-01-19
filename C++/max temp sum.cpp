#include <iostream>

using namespace std;
int main(int argc, char *argv[]) {
	freopen("input.txt", "rt", stdin);
	int num_temp_data=0;
	int consecutive_qty=0;
	
	//Variable distribution from input source
	scanf("%d", &num_temp_data);
	scanf("%d", &consecutive_qty);
	
	int temp_data[num_temp_data];
	for(int i=0; i<num_temp_data; i++){
		scanf("%d", &temp_data[i]);
	}

	//define sum, sum_qty
	int sum_qty = num_temp_data - consecutive_qty;
	int sum_max = -2147000000;
	
	for(int i=0; i<=sum_qty; i++){
		int temp_sum = 0;
		for(int j=i; j<i+consecutive_qty; j++){
			temp_sum+=temp_data[j];
		}
		
		if(sum_max<temp_sum){sum_max=temp_sum;}
	}

	cout << sum_max << endl;
	
}