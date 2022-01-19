#include <iostream>

using namespace std;

struct Rectangle 
{
	int length;
	int width;
};

enum StudentName
{
	JACKJACK,
	DASH,
	VIOLET,
};


int main(int argc, char *argv[]) {
	
	int num_students;
	cin >> num_students;
	
	int students_scores[num_students];
	for (int i=0; i<num_students; i++)
		{cout  << students_scores[i] << endl;}
//	int my_array[]{1, 2, 3, 4, 5};
//	
//	for (int i=0;i<=4;i++){cout  << my_array[i] << endl;}
//	cout << my_array[JACKJACK] << endl;

//	cout << sizeof(Rectangle) <<endl;
//	
//	Rectangle rect_arr[10];
//	
//	cout << sizeof(rect_arr) << endl;
}