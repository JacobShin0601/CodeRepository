#include <iostream>
#include <vector>

using namespace std;

vector<int> total_number (int n){
	std::vector<int> total_number;
	int i;
	
	for (i=0; i<n; i++){
		total_number[i] = i+1;
	}
	
	return total_number;
}

int total_type_in_number (int x){
	int type_in_cnt = 0;
	while(x>0){
		x=x%10;
		type_in_cnt++;
	}
	
	return type_in_cnt;
}

int main(int argc, char *argv[]) {
	int n;
	cin >> n;
	
	std::vector<int> total_number(n);
	
	int i=0;
	int total_count = 0;
	
	for (i=0; i<n; i++){
		int temp = total_type_in_number(i);
		total_count += temp;
	}
	
	cout << total_count << endl;
}