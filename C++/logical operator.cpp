#include <iostream>

using namespace std;
int main(int argc, char *argv[]) {
//	bool x = true;
//	bool y = false;
	
//	cout << (x&&y) << endl;
//	
//	bool hit = true;
//	int health = 10;
//	
//	if (hit == true && health < 20)
//	{
//		cout << "die" << endl;
//	}
//	else {
//		health -= 20;
//	}
	
//	cout << (x||y) << endl;
//	
//	
//	int x = 5;
//	int y = 7;
//	
//	if(x != y)
//	{
//		cout << " x is not equal to y" << endl;
//	}
//	else {
//		cout << " x is equal to y" << endl;
//	}
	
//	int v = 1;
//	if (v == 0 || v == 1)
//		cout << "v is 0 or 1" << endl;
//	
//	return 0;

//int x = 2;
//int y = 2;
//
//if (x == 1 && y ++ == 2){
//	//do something
////	cout << y << endl;
//}
//	cout << y << endl;
	
	
//	bool x = true;
//	bool y = false;
//	
//	!(x && y);
//	!x && !y;
	
//	bool x = true;
//	bool y = false;
//	
//	cout << (x != y) << endl;
//	
	
	
	
	bool v1 = true;
	bool v2 = false;
	bool v3 = false;
	
	bool r1 = v1 || v2 && v3;
	bool r2 = (v1 || v2) && v3;
	bool r3 = v1 || (v2 && v3);
	
	cout << r1 << endl;
	cout << r2 << endl;
	cout << r3 << endl;
}
