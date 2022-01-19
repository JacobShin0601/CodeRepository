#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
	const int num_rows = 3;
	const int num_columns = 5;
	
//	for (int i = 1; i < num_rows+1; ++i){
//
//		for (int j = 1; j <num_columns+1; ++j){
//			cout << "[" << i << "]" << "[" << j << "]" << " ";
//		}
//		cout << endl;
//	}
	
	int array[num_rows][num_columns] = {
		{3, 5, 7, 9, 11},
		{2, 4, 6, 8, 10},
		{11, 13, 15, 17, 19},
	};
	
	for(int row = 0; row < num_rows; ++row){
		for (int col = 0; col < num_columns; ++col){
			cout << array[row][col] << '\t';
		}
		cout << endl;
	}
}