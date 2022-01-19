#include <iostream>
#include <array>
#include <tuple>

using namespace std;

//int& get(std::array<int, 100> &my_array, int idx){
//	return my_array[idx];
//}

std::tuple<int, double> getTuple(){
	int a = 10;
	double d = 3.14;
	return std::make_tuple(a, d);
}
//int getValue (int x) {
//	int value = x*2;
//	return value;
//}

//int *allocateMemory(int size){
//	return new int[size];
//}

int main(int argc, char *argv[]) {
//	int value = getValue(3);
//	
	
//	int *arr = allocateMemory(1024);
//	return 0;
	
//	std::array<int, 100> my_array;
//	my_array[30] = 10;
//	get(my_array, 30) *= 10;
//	
//	cout << my_array[30] << endl;
	
	std::tuple<int, double> my_tp = getTuple();
	cout << std::get<0>(my_tp) << endl;
	cout << std::get<1>(my_tp) << endl;
	
	return 0;
	
}