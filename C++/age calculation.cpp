#include <stdio.h>
#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	freopen("input.txt", "rt", stdin);
	
	char regi_num[20];
	int current_year;
	int born_year;
	int age;
	
	scanf("%s", regi_num);
	
	///////// age calculcation
	if(regi_num[7]=='1' || regi_num[7]=='2'){
		born_year = 1900 + ((regi_num[0]-48)*10+(regi_num[1]-48));
	}
	
	
	////////// age print
	age = 2019 - born_year + 1;
	printf("%d ", age);
	
	
	//////////M, W description
	if(regi_num[7]=='1' || regi_num[7]=='3'){
		printf("M\n");
	}
	else {printf("W\n");}
	
}