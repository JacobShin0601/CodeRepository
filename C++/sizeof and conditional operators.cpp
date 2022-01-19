#include <iostream>
#include <cmath>

using namespace std;
int main(int argc, char *argv[]) {
	
//	float a;
//	
//	cout << sizeof(float) << endl;
//	cout << sizeof(a) << endl;

//	int a = 1, b = 10;
//	int z;
//	
//	z = (a, a + b++);
//	z;
//	return 0;
	
	
	//arithmetic if, conditional operator
	bool onSale = true;
	
//	int price;
//	
//	if(onSale)
//		price = 10;
//	else
//		price = 100;

//	const int price = (onSale == true)? 10 : 100;
//	cout << price << endl;
	
//	
//	int x = 5;
//	cout << ((x % 2 == 0) ? "even" : "odd") <<endl;
//	
	
	double d1 (100 - 99.99); // 0.001
	double d2 (10 - 9.99); 	// 0.001
	
	
	cout << d1 << endl;
	cout << d2 << endl;
	
	const double epsilon = 1e-10;
	
	if (std::abs(d1-d2) < epsilon)
		cout << "Approximately equal" << endl;
	else
		cout << "not equal" << endl;
	cout << d1 - d2 << endl;
	
	
//	cout << std::abs(d1-d2) << endl;
//	
//	if(d1 == d2)
//		cout << "equal" << endl;
//	else
//		{
//			cout << "not equal" << endl;
//			if (d1 > d2)
//				cout  << "d1 > d2" << endl;
//			else
//				cout << "d1 < d2" <<endl;
//		}
	return 0;
				
}