#include <iostream>
using namespace std;

// notice this & 
void duplicate(int& a, int& b, int& c){
	a*=2;
	b*=2;
	c*=2;
}


int main (){
	int x = 1;
	int y = 3;
	int z = 7;

	duplicate(x,y,z);

	cout << "x: " << x << " y: " << y <<" z: " << z;
	return 0;
}
