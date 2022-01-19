//#include <iostream>
//#include <string>
//#include <fstream>
#include <stdio.h>

using namespace std;


int main(int argc, char *argv[]) {
//	wstring input_source;
//	std::ifstream readFile;
//	readFile.open("input.txt");
//	if(readFile.is_open()){
//		while(!readFile.eof()){
////			string input_source;
//			getline(readFile, input_source);
//		}
//		readFile.close();
//	}
	
//	freopen("input.txt", "rf", stdin);
	
	char input_source[100];
	char restored_text[100];
	
//	fgets(input_source, 100, stdin);
//	scanf("%s", input_source); /// scanf's delimeter : space
//	gets(input_source, 100) // delimeter is the line change
//	std::getline (stdin, input_source);
//	getline(cin, input_source);

	
	int i, cnt = 0;
	for (i=0; input_source[i]!='\0'; i++){
		if(input_source[i] != ' '){
			if (65 <= input_source[i] && input_source[i] <= 90){
				restored_text[cnt++] = input_source[i]+32;// 32 is the number making capital to lowercase
			}//Capital letter extraction from 65(A)
			else {
				restored_text[cnt++] = input_source[i]+32;
			}// original lowercase, no need to transfer it to capital
			
		}// filtering space
	}// for loop (search and return to restored mode)
	restored_text[cnt] = '\0';
	
	printf("%s\n", restored_text);
	return 0;
}