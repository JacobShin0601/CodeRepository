#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int main(int argc, char *argv[]) {
	freopen("input.txt", "rt", stdin);
	int num_input;
	scanf("%d", &num_input);
	
	vector<int> sorted_vector(0);
	queue<int> neg_queue;
	queue<int> pos_queue;
	
	for(int i=0; i<num_input; i++){
		int temp;
		scanf("%d", &temp);
		if(temp < 0){
			neg_queue.push(temp);
		}
		else if(temp >= 0){
			pos_queue.push(temp);
		}
	}
	
	bool neg_F = false;
	bool pos_F = false;
//	int s_neg = neg_queue.size();
//	int s_pos = pos_queue.size();
//	
	while(neg_F!=true){
		int temp = neg_queue.front();
		sorted_vector.push_back(temp);
		neg_queue.pop();
		neg_F = neg_queue.empty();
	}
	
	while(pos_F!=true){
		int temp = pos_queue.front();
		sorted_vector.push_back(temp);
		pos_queue.pop();
		pos_F = pos_queue.empty();
	}
	
	for(int i=0; i<num_input; i++){
		cout << sorted_vector[i] << " ";
	}
	
}