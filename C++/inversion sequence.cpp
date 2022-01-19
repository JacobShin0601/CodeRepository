#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	//making and distribute inputs to variables
	freopen("input.txt", "rt", stdin);
	int num_element;
	scanf("%d", &num_element);
	std::vector<int> inversion_sequence(num_element);
	std::vector<int> original_sequence(num_element);

	for(int i=0; i<num_element; i++){
		int temp;
		scanf("%d", &temp);
		inversion_sequence[i]=temp;
		original_sequence[i]=-1;
	}
	
	int blank;
	
	for(int i=0; i<num_element; i++){
		int cnt=0;
		blank=inversion_sequence[i]+1;
		//original_sequence[blank]=i+1;
		for(int j=0; j<num_element; j++){
			if(original_sequence[j]==-1){
				cnt++;
				if(cnt==blank){
					original_sequence[j]=i+1;
					break;
				}
			}
		}
	}
	
	for (int i=0; i<num_element; i++){
		cout << original_sequence[i] << " ";
	}
	
}