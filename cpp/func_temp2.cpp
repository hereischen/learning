#include <iostream>
using namespace std;

template <class T, class U>
bool are_eq(T a, U b)
{
	return (a==b);
} 

int main(){
	if (are_eq(10, 10.0)){
		cout << "these two are equal\n ";
	} else {
		cout << "these are not equal\n";
	}
	return 0;
}