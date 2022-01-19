#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
	std::vector<int> my_vector {1, 2, 3, 4, 5};
	
	for (auto &itr : my_vector){
		cout << itr << " ";
		itr++;
	}
	cout << endl;
	
	my_vector.resize(10);
	cout << my_vector.size() << endl;
	
	cout << my_vector[1] << " " << my_vector.at(1) << endl;
}