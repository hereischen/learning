#include <iostream>
using namespace std;

// 不换行真是太坑了
int main () {
	int a [] = {1,1,1, 1};
	int n, result=0;

	for (n=0;n<4;n++){
		cout << n << "\n";
		result+= a[n];
		cout << "this result " << result << '\n';
	}
	cout << "result " << result;
	return 0;
}