#include <iostream>

using namespace std;
int main(int argc, char *argv[]) {
//	int x, y;
//	cin >> x >> y;
//	
//	if (x > 0 && y > 0)
//		cout << "both numbers are positive" << endl;
//	else if (x > 0 || y > 0)
//		cout << "One of the numbers is positive" << endl;
//	else
//		cout << "both numbers are negative" << endl;
	
	int x;
	cin >> x;
	
	if (x>10)
		cout << "A" << endl;
	else if (x == -1)
		return 0;
	else if (x < 0)
		cout << "B " << endl;
	
	return 0;
}
