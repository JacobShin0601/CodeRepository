#include <iostream>
#include <cassert>

using namespace std;

class MyString{
//private:
public:
	char *m_data = nullptr;
	int m_length=0;
	
public:
	MyString(const char* source=""){
		assert(source);
		
		m_length = std::strlen(source) + 1;
		m_data = new char [m_length];
		
		for (int i = 0; i < m_length; ++i){
			m_data[i] = source[i];
		}
		
		m_data[m_length-1] = '\0';
		
		
	}
	
}

int main(int argc, char *argv[]) {
	
}