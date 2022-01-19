#include <iostream>
#include <vector>

using namespace std;
int main(int argc, char *argv[]) {
	//inserting input into variable and vector
	freopen("input.txt", "rt", stdin);
	
	int size_progression=0;
	scanf("%d", &size_progression);
	
	std::vector<int> progression_vector(size_progression);
	for(int i=0; i<size_progression; i++){
		int temp;
		scanf("%d", &temp);
		progression_vector[i]=temp;
	}
	
	//find incremental part, and compare maximum value
	int max_incremental_part=0;
	bool loop_flag=true;
	int cnt=0;
	
	for(int i=0; i<size_progression; i++){
		cnt++;
		if(progression_vector[i]>progression_vector[i+1]){cnt=1; continue;}
		else if(progression_vector[i]<=progression_vector[i+1]){
			if(max_incremental_part<cnt){max_incremental_part=cnt;}
			continue;
		}
	}
	
	cout << max_incremental_part << endl;
}