#include <iostream>
#include <vector>


using namespace std;

int main(int argc, char *argv[]) {
	int i, j, n, m, v_size, sum = 0;
	
	std::vector<int> v = {};
	
	cin >> n;
	
	for (i=1; i<n; i++){
		if (n%i==0){
			sum += i;
			v.push_back(i);
			v_size++;
			
		} // if print i
	} // for vector loop

//	m = sizeof(v);

	
	for (j=1; j<=v_size; j++){
		cout << v[j-1] << " ";
		
		if (j!=v.back()) {
			cout << "+" << " ";
		}
	}//cout array
	cout << "=" << " " << sum << endl;
}