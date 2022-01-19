#include <iostream>

using namespace std;

class Something{
public:
	int m_value = 0;
	void setvalue(int value){m_value = value;}
	int getvalue() const {return m_value;}
};

void print (Something st){
	cout << st.m_value << endl;
}

int main(int argc, char *argv[]) {
	
	const Something something;
//	something.setvalue(3);
	
	cout << something.getvalue() << endl;
	
	return 0;
}