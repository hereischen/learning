#include <iostream>
using namespace std;

int opreate (int x, int y){
	return (x+y);
}

double opreate (double x, double y){
	return x*y;
}

int main () {
	int a = 2, b = 3;
	double c = 2.0, d = 3.0;
	auto z = opreate(a,b);
	cout << "you got: " << z  << "\n";
	z = opreate(c,d);
	cout << "z = " << z;
	return 0;
}