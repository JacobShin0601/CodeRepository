#include "Monster.h"

using namespace std;

int main(int argc, char *argv[]) {
	Monster mon1 ("Sanson", Position2D(0, 0));
	
	mon1.moveTo(Position2D(1, 2));
	
	cout << mon1 << endl;
}