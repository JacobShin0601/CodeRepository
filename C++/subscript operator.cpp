#include <iostream>

using namespace std;

class IntList{
private:
	int m_list[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
	
public:
//	void setItem(int index, int value){
//		m_list[index] = value;
//	}
//	
//	int getItem(int index){
//		return m_list[index];
//	}
//	
//	int* getList(){
//		return m_list;
//	}
	
	const int& operator [] (const int index) const{
		assert(index >= 0);
		assert(index < 10);
		
		return m_list[index];
	}
};

int main(int argc, char *argv[]) {

	const IntList my_list;
//	my_list[3] = 10;
	cout << my_list[3] << endl;
//	my_list.setItem(3, 1);
//	cout << my_list.getItem(3) << endl;
//	my_list.getList()[3] = 10;
//	cout << my_list.getList()[3] << endl;
	
}