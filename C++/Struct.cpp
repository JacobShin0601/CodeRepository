#include <iostream>

using namespace std;


//void printPerson(double height, float weight, int age) {
//	
//}

struct Person {
	double height;
	float weight;
	int age;
	string name;


//void printPerson(Person ps){
//	cout << ps.height << " " << ps.weight << " " << ps.age << " " << ps.name << endl;
//}

void print(){
	cout << height << " " << weight << " " << age << " " << name << endl;
}
};

int main(int argc, char *argv[]) {
	Person me;
	me.age = 20;
	me.name = "Jack Jack";
	me.height = 2.0;
	me.weight = 100.0;
	
	Person me2 = me;
	me2.print();
	
	Person mom{1.6, 50.0, 42, "Anna"};

	Person dad;
	
}