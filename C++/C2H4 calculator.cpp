#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[]) {
	freopen("input.txt", "rt", stdin);
	
	char compound_string[10];
	int num_C=0, num_H=0, i, pos;
	scanf("%s", compound_string);
	
	// calculating C 
	if(compound_string[1]=='H'){
		num_C = 1;
		pos = 1;
	}
	else {
		for(i=1; compound_string[i]!='H'; i++){
			num_C=num_C*10+(compound_string[i]-48);
		}
		pos = i; // position of H
	}
	
	//calculating H
	if(compound_string[pos+1]=='\0') {
		num_H = 1;
	}
	else{
		for (int j=i+1;compound_string[j]!='\0';j++){
			num_H = num_H*10+(compound_string[j]-48);
		}
	}
	
	int result = num_C*12 + num_H;
	cout << result << endl;
	return 0;
	
}