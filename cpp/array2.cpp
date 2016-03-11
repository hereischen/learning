#include <iostream>
#include <array>
using namespace std;

int main() {
	array<int,3> myarray = {1,2,3};

	for (int i=0; i<myarray.size();i++){
		myarray[i]++;
	}

	for (int elem : myarray){
		cout << elem << "\n";
	}
}

