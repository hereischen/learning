#include <iostream>
using namespace std;

template <class T>
T sum (T a, T b)
{ 
	T result;
	result = a + b;
	return result;
}

int main  () {
	int a =1, b=2, x;
	double c =2.0, d = 3.5, y;
	x =sum<int>(a,b);
	cout << "int " << x << "\n";
	y = sum<double>(c,d);
	cout << "double " << y << "\n";
	return 0;
}

