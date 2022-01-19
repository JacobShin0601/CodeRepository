#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	freopen("input.txt", "rt", stdin);
	int size_cache, num_process;
	//int num_work; 1-100
	
	cin >> size_cache;
	cin >> num_process;
	vector<int> cache(size_cache);
	vector<int> input_of_work(num_process);
	
	for(int i=0; i<num_process; i++){
		int temp;
		scanf("%d", &temp);
		input_of_work[i] = temp;
	}
	
	// cache hit
	for (int i=0; i<num_process; i++){
		bool cache_hit = false;
		
		if(input_of_work[i]==cache[0]){continue;} // if the first item of cache is as same as the item of input of work, then go to just next item of input of work.
		for(int j=size_cache-1; j>0; j--){
			if(input_of_work[i]==cache[j]){ // if cache item of inner loop is as same as input of work, then just push each item to the next
				for(int k=j; k>=0; k--){
					cache[k]=cache[k-1];
				}
				cache[0]=input_of_work[i];
				cache_hit = true;
				break;
			}
		}
		if(cache_hit==false){ // cache miss
			for(int j=size_cache-1; j>=0; j--){
				//int temp = cache[j];
				cache[j] = cache[j-1];
			}
			cache[0] = input_of_work[i];
		}
//		for(int i=0; i<size_cache; i++){
//			cout << cache[i] << " ";
//		}
//		cout << endl;
	} // outter for loop is terminated
	
	for(int i=0; i<size_cache; i++){
		cout << cache[i] << " ";
	}
}