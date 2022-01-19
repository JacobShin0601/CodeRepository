#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	freopen("input.txt", "rt", stdin);
	int num_input, input;
	scanf("%d", &num_input);
	vector<int> unordered_vector(num_input);
	scanf("%d", &input);
	
	for(int i=0; i<num_input; i++){
		scanf("%d", &unordered_vector[i]);
	}
	std::vector<int> ordered_vector(num_input); 
	sort(unordered_vector.begin(), unordered_vector.end());
	ordered_vector = unordered_vector;

	int left_pnt=0, right_pnt = num_input-1;
	
	while(left_pnt<=right_pnt){
		int mid_pnt = (left_pnt+right_pnt)/2;
		if(input==ordered_vector[mid_pnt]){
			cout << input << " is located in " << mid_pnt+1 << " place";
			break;
		}
		else if(input<ordered_vector[mid_pnt]){
			right_pnt = mid_pnt-1;
		}
		else{left_pnt=mid_pnt+1;}
	}
	return 0;
	
//	int pnt = 1;
//	for(int i=0; i<num_input; i++){
//		if(input==unordered_vector[i]){cout << pnt << endl; break;}
//		else if(input>unordered_vector[i]){pnt++;}
//	}
	
}