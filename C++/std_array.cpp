#include <iostream>
#include <array>

using namespace std;
int main(int argc, char *argv[]) {
	std::array<int, 5> abc = {8654, 130, 55893, 25, 5512};
	
	for (auto element : abc) {
		cout << element << " ";
	}
	
	cout << endl;
	
	std::sort(abc.begin(), abc.end());
	
	for (auto element : abc) {
		cout << element << " ";
	}

	return 0;
}
