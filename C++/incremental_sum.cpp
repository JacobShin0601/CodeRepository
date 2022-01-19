#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	double input;
	
	cin >> input;
	
	auto cnt=0;
	double temp = 1;
	
	while(true){
		if(temp<=0){break;}
		for(double n=2; n<1000; n++){
			if(temp<=0){break;}
			double x=0;
			
			temp = (input-(n*(n-1)/2))/n;
			if(temp==static_cast<int>(temp)){x=temp;}
			if(x!=0){cout << x ;
				int i;
				for(i=x+1; i<x+n; i++){
					cout << " + " << i;
				}
				if(x!=0){cout << " = " << input << endl;cnt++;}
			}
		}
	}
	
	cout << "all combinations : " << cnt << endl;
	
	return 0;
}