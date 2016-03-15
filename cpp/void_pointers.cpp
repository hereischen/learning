#include <iostream>
using namespace std;

//the null pointer value
int * p = 0;
int * q = nullptr;

void increase (void * data, int psize)
{
	if (psize == sizeof(char))
	{
		cout << sizeof(char);
		char * pchar;
		pchar = (char*) data; ++(*pchar); 
	}
	else if (psize == sizeof(int))
	{
		cout << sizeof(int);
		int* pint; pint=(int*)data; ++(*pint);
	}
}

int main ()
{
  char a = 'x';
  int b = 1602;
  increase (&a,sizeof(a));
  increase (&b,sizeof(b));
  cout << a << ", " << b << '\n';
  return 0;
}