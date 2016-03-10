#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(){
	string mystr;
	float price;
	int quantity;

	cout << "Pirce? ";
	getline(cin, mystr);
	stringstream (mystr) >> price;
	cout << "Quantity? ";
	getline(cin,mystr);
	stringstream (mystr) >> quantity;
	cout << "You have spent " << price* quantity << endl;
	return 0;
}