#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	int num_clip, num_DVD;
	freopen("input.txt", "rt", stdin);
	scanf("%d", &num_clip);
	scanf("%d", &num_DVD);
	std::vector<int> clip_vector(num_clip);
	int total_time_clip = 0;
	for(int i=0; i<num_clip; i++){
		scanf("%d", &clip_vector[i]);
		total_time_clip+=clip_vector[i];
	}
	
	//we're going to calculate the minimum time for the each DVD in the given number of DVD.
	int left_pnt = 1;
	int right_pnt = total_time_clip;
	int min_result=100000;
	int max_clip = clip_vector[num_clip-1];
	
	while(left_pnt<=right_pnt){
		int mid_pnt = (left_pnt+right_pnt)/2; // in case of input.txt, it's 23
		if(max_clip>mid_pnt){left_pnt++; continue;}
		 
		int temp_sum=0;
		int temp_cnt=1;
		for(int i=0; i<num_clip;i++){
			if(temp_sum+clip_vector[i]<=mid_pnt){
				temp_sum+=clip_vector[i];
			}
			else if(temp_sum+clip_vector[i]>mid_pnt){
				temp_cnt++;
				temp_sum=0;
				temp_sum+=clip_vector[i];
			}
		}
		if(temp_cnt<=num_DVD){
			min_result=mid_pnt;
			right_pnt=mid_pnt-1;
		} 
		else{left_pnt=mid_pnt+1;}
	}

	cout << min_result << endl;
	
	return 0;
}