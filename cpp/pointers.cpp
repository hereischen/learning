#include <iostream>
using namespace std;

int main (){
	int first, second;
	int * mypointer;

	mypointer = &first; // mypointer is addres of first
	*mypointer = 20; // value pointed to by my pointer is 20

	mypointer = &second; // mypointer is addres of second

	cout << "First is " << first << "\n";
	cout << "my pointer is " << mypointer << "\n";

}