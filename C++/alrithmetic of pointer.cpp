#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
//	double value = 7;
//	double *ptr = &value;
//	
//	cout << ptr << endl;
//	cout << uintptr_t(ptr-1) << endl;
//	cout << uintptr_t(ptr) << endl;
//	cout << uintptr_t(ptr+1) << endl;
//	cout << uintptr_t(ptr+2) << endl;
	
//	int array[] = {9, 7, 5, 3, 1};
//	
//	int *ptr = array;
//	
//	for (int i = 0; i < 5; i++){
//		//cout << array[i] << " " << (uintptr_t)&array[0] <<endl;
//		cout << *(ptr+i) << " " << (uintptr_t)(ptr+i) << endl;
//	}
	
	
	char name[] = "Jack Jack";
	const int n_name = sizeof(name) / sizeof(char);
	char *ptr = name;
	
	for (int i = 0; i < n_name; ++i) {
		cout << *(ptr + i) << " " << endl;
	}
}