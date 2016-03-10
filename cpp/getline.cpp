#include <iostream>
#include <string>

using namespace std;

int main(){
	string mystr;
	cout << "What's your name mate? ";
	getline(cin, mystr);
	cout << "Hello! " << mystr << "\n";
	cout << "What's your favorate language, " << mystr << "?\n";
	getline(cin, mystr);
	cout << mystr << "? Cool,mate!" ;
	return 0;

}

