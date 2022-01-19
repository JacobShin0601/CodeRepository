#include <iostream>
#include <limits>

using namespace std;
int main(int argc, char *argv[]) {
	const int fibonacci[] = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89};
	
//	for (int number : fibonacci)
//		cout << number << " ";
//	cout << endl;
	int max_number = std::numeric_limits<int>::lowest();
	
	for (const auto &n : fibonacci)
		max_number = std::max(max_number, n);
	cout << max_number << endl;
}