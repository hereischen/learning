#include <iostream>
using namespace std;

int addition (int a, int b){
	int c;
	c =a + b;
	return c;
}

int main() {
	int z;
	z = addition(5,3);
	cout << "you got " << z;
}