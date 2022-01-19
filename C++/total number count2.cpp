#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
	int n;
	cin >> n;
//	freopen("input.txt", "rf", stdin);
	
	std::vector<int> number_vector;
	int i, j;
	for (i=0; i<n; i++){
		number_vector.push_back(i+1);
	} // for loop generating num_vector;
	
	int total_count = 0;
	int temp = 0;
	for (vector<int>::iterator itr = number_vector.begin(); itr!=number_vector.end();){
		temp = *itr;
		
		while(temp>0){
			total_count++;
			temp = temp/10;
		}
		itr++;
	}
	
	cout << total_count << endl;
	return 0;
}