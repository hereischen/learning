#include <iostream>
#include <string>
using namespace std;


int main(){
	char question1 [] = "What's your name?";
	string question2  = "Where are you from?";
	
	char answer1 [80];
	string answer2;

	cout << question1;
	cin >> answer1;
	cout << question2;
	cin >> answer2;

	cout << "Hello! " << answer1 << "\n";
	cout << "From " << answer2 << "\n";
}