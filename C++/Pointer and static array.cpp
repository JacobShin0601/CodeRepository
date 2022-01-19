#include <iostream>

using namespace std;


struct MyStruct{
	int array[5] = {9, 7, 5, 3, 1};
};

void doSomething(MyStruct *ms){
	cout << sizeof((*ms).array) << endl;
}

void printArray(int *array){
	cout << sizeof(array) <<endl;
}

int main(int argc, char *argv[]) {
//	int array[5] = {9, 7, 5, 3, 1};
////	
////	cout << array[0] << " " << array[1] << endl;
////	cout << array << endl;
////	cout << &(array[0]) << endl;
////	cout << *array << endl;
////	
////	char name[] = "jackjack";
////	cout << *name << endl;
////	
//	int *ptr = array;
//	cout << sizeof(ptr) << endl;
//	
//	printArray(array);
	
	MyStruct ms;
	cout << ms.array[0] << endl;
	cout << sizeof(ms.array) << endl;
	doSomething(&ms);
	return 0;
}