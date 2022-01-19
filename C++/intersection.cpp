#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;
int main(int argc, char *argv[]) {
	
	freopen("input.txt", "rt", stdin);
	int num_v_A, num_v_B;
	
	scanf("%d", &num_v_A);
	std::vector<int> v_A(num_v_A);
	for(int i=0; i<num_v_A; i++){
		scanf("%d", &v_A[i]);
	}
	scanf("%d", &num_v_B);
	std::vector<int> v_B(num_v_B);
	for(int i=0; i<num_v_B; i++){
		scanf("%d", &v_B[i]);
	}
	
	int num_v_C=num_v_A+num_v_B;
	std::vector<int> v_C(num_v_C);
	
	int point_v_A=0, point_v_B=0, point_v_C=0;
//	for(int i=0; i<num_v_C; i++){			
//		if(v_A[point_v_A]!=v_A.back()){
//			if(v_A[point_v_A]<=v_B[point_v_B]){
//				if(num_v_A!=point_v_A) v_C[i]=v_A[point_v_A++];
//			}
//		}
//		else{
//			if(num_v_B!=point_v_B) v_C[i]=v_B[point_v_B++];
//		}
//		cout << v_C[i] << " ";
//	}
	
	while(point_v_A<=num_v_A && point_v_B<=num_v_B){
		if(point_v_A!=num_v_A && point_v_B!=num_v_B){
			if(v_A[point_v_A]<v_B[point_v_B]){
				v_C[point_v_C++] = v_A[point_v_A++];
			}
			else{
				v_C[point_v_C++] = v_B[point_v_B++];
			}
		}
		else if(point_v_A==num_v_A && point_v_B==num_v_B){break;}
		else{
			while(point_v_A<num_v_A){
				v_C[point_v_C++] = v_A[point_v_A++];
//				if(point_v_A==num_v_A){break;}
			}
			while(point_v_B<num_v_B){
				v_C[point_v_C++] = v_B[point_v_B++];
//				if(point_v_B==num_v_B){break;}
			}
		}
	}
	
	for(int i=0; i<num_v_C; i++){
		cout << v_C[i] << " ";
	}
	
	return 0;
}