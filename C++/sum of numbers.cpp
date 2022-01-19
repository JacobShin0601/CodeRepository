#include <stdio.h>
#include <iostream>

using namespace std;

int summary_of_number (int x) {
	int i=1;
	int result = 0;
	
	for (i=1; i<=x; i++){
		result += i;
	}

	return result;
}

int main(int argc, char *argv[]) {
	int students_cnt=0;
	int num_card=0;
	int sum_of_num=0;
	int i=0;
	
	//initial setting (input file reading, setting number of students)
	freopen("input.txt", "rt", stdin);
	scanf("%d", &students_cnt);
	//cin >> students_cnt;
	
	
	// input -> number card array
	for(i=1; i<=students_cnt; i++){
		scanf("%d %d", &num_card, &sum_of_num);
//		cin >> num_card >> sum_of_num;
		
		if(sum_of_num==summary_of_number(num_card)){printf("Yes\n");}
		else {printf("No\n");}
	}
	return 0;
}