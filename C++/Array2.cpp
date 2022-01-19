#include <iostream>

using namespace std;


void doSomething(int students_scores[])
{
	cout << (size_t)&students_scores << endl;
	cout << (size_t)students_scores << endl;
	cout << students_scores[0] << endl;
	cout << students_scores[1] << endl;
	cout << students_scores[2] << endl;
}

int main(int argc, char *argv[]) {
	const int num_students(20);
	
	int students_scores[num_students] {1, 2, 3, 4, 5, };
	
	cout << (size_t)&students_scores << endl;
	cout << students_scores[0] << endl;
	cout << students_scores[1] << endl;
	cout << students_scores[2] << endl;
	
	cout << endl;
	
	doSomething(students_scores);
	
}