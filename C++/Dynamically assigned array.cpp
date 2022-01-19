#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	int length;
	
	cin >> length;
	
	int *array = new int[length]{11, 22, 33, 44, 55, 666};
	
	array[0]=1;
	array[1]=2;
	
	for(int i = 0; i < length; ++i){
		cout << array [i] << endl;
		cout << (uintptr_t)&array [i] << endl;
	}
	
	return 0;
}