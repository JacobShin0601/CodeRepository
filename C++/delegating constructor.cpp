#include <iostream>
#include <string>

using namespace std;

class Student{
private:
	int m_id;
	string m_name;
	
public:	
	Student(const string& name_in)
		:Student(0, name_in)
	{}
	
	Student(const int& id_in, const string& name_in)
		: m_id(id_in), m_name(name_in)
	{}
	
	void print(){
		cout << m_id << " " << m_name << endl;
	}
};


int main(int argc, char *argv[]) {
	Student st1(0, "Jack Jack"); 
//	Student st2(2, "Mike");
	
	st1.print();
//	st2.print();
	

	
}