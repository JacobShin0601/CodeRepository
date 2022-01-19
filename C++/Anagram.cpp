#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	char input_string[100];
	int string1[60]={0,};
	int string2[60]={0,};
	int i=0, j=0, m=0;
	
	freopen("input.txt", "rf", stdin);
	
	// first input to string 1
	scanf("%s", input_string);
	for(i=0; input_string[i]!='\0'; i++){
		if(65<=input_string[i] && input_string[i]<=90){
			string1[input_string[i]-64]++;
		}
		else {string1[input_string[i]-69]++;}
	}//for loop 
	
	// second input to string 2
	scanf("%s", input_string);
	for(j=0; input_string[j]!='\0'; j++){
		if(65<=input_string[j] && input_string[j]<=90){
			string2[input_string[j]-64]++;
		}
		else {string2[input_string[j]-69]++;}
	}//for loop 
	
	//print out result
	for(m=0; m<=52; m++){
		if(string1[m]!=string2[m]){
			cout << "No" << endl;
			exit(0);
		}
	}
	cout << "Yes" << endl;
	
}