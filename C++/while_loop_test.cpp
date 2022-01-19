#include <iostream>

using namespace std;
int main() {
	
	cout << "While loop test" << endl;
	
	int outer_count = 5;
	
	while (outer_count >= 1)
	{
		int inner_count = 1;
		
		while (inner_count <= outer_count)
		{
			cout << inner_count++ <<" ";
		}
		
		cout << endl;
		outer_count--;
		
		}
	}
	
	
//	int count = 1;
//	
//	while (count < 100)
//	{
//		if (count %5 == 0) cout << "Hello" << count << endl;
//		
//		count++;
//	}
//	return 0;
	
	
//	
//	unsigned int count = 10;
//	
//	while (count >= 0)
//	{
//		if (count == 0) cout << "Zero";
//		else cout << count <<" ";
//		count--;
//	}
	
//	int count = 0;
//	while(count<10)
//	{
//		cout << count << endl;
//		++count;
//	}
//	return 0;
	
