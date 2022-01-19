#include <iostream>
#include <cstdarg>

using namespace std;

double findAverage(int count, ...){
	double sum = 0;
	
	va_list list;
	
	va_start(list, count);
	
	for (int arg = 0; arg < count; ++arg){
		sum += va_arg(list, int);
	}
	
	va_end(list);
	
	return sum / count;
}

int main(int argc, char *argv[]) {
	cout << findAverage(1, 1, 2, 3) << endl;
	cout << findAverage(2, 1, 2) << endl;
	cout << findAverage(5, 1, 2, 3) << endl;
}