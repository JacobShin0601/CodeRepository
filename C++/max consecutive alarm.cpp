#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;
int main(int argc, char *argv[]) {
	int input_size = 0;
	int limit = 0;
	std::vector<int> measurement;
	int i = 0;
	
	freopen("input.txt", "rt", stdin);
	scanf("%d %d", &input_size, &limit);
	
	//making measurement vector
	for(i=1; i<=input_size; i++){
		int temp = 0;
		scanf("%d", &temp);
		measurement.push_back(temp);
	}
	
	int count = 0;
	int max = -2147000000;
	for (int e:measurement){
		if(e<limit){
			count = 0;
		}
		else{
			count++;
			if(max<count){
				max = count;
			}//setting max if
		}//counting alarm else
	}//measurement vector loop
	cout << "Maximum sec of alarm is : " << max << endl;
}