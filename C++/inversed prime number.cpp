#include <iostream>
#include <stack>
#include <string>

using namespace std;

int reversed_number(int x){
	int result = 0;
	
	while (x>0){
		int tmp = x%10;
		result = result*10 + tmp;
		x = x/10;
	}
	
	return result;
}




//int reversed_number (int x){
//	int result = 0;
//	std::string temp_result;
//	std::stack<char> temp_stack;
//	std::string temp_string = std::to_string(x);
//	
//	int size = sizeof(temp_string);
//	
//	for (int i=0; i<size; i++){
//		temp_stack.push(temp_string[i]);
//	}
//	
//	for (int j=0; j<size; j++){
//		temp_result.push_back(temp_stack.top());
//		temp_stack.pop();
//	}
//	
//	cout << temp_result << endl;
//	
//}

bool isPrimeNumber(int x){
	int i;
	
	if(x==1){ return false;}
	
	bool flag = true;
	
	for (i=2; i<x; i++){
		if(x%i==0){
			flag = false;
			break;
		}
	}
	
	return flag;
}

int main(int argc, char *argv[]) {
	freopen("input.txt", "rf", stdin);
	int tmp, i, n, num;
	scanf("%d", &n);
	
	for(i=1; i<=n; i++){
		scanf("%d", &num);
		tmp = reversed_number(num);
		
		if (isPrimeNumber(tmp)){
			printf("%d ", tmp);
		}
	}
	
	return 0;

//	reversed_number(3456);
	
}