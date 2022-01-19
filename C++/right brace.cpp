#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	int left_cnt = 0, right_cnt = 0, i;
	char input_source[100];
	freopen("input.txt", "rf", stdin);
	
	scanf("%s", input_source);
	
	int balance_result = left_cnt - right_cnt;
	for (i=0; input_source[i]!='\0'; i++){
		if (balance_result < 0) {cout << "Abnormal"; break;}
		if(input_source[i]==')'){
			right_cnt++;
		}
		if(input_source[i]=='('){
			left_cnt++;
		}
	}//for loop for scanning characters
	
	
	///print out result

	if (balance_result==0){
		cout << "These are perfect braces" << endl;
	}
	else{cout << "These are not perfect braces" << endl;}
}