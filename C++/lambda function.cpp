#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
	vector<int> v;
	v.push_back(1);
	v.push_back(2);
	v.push_back(3);
	
	auto func2 = [](int val) {cout << val << endl;};
	for_each(v.begin(), v.end(), func2);
	
	cout << []() -> int {return 1;}() << endl;
	
	std::function<void(int)> func3 = func2;
	func3(123);
	
	std::function<void(void)> func4 = std::bind(func3, 456);
	func4();
	
}