#include <stdio.h>
#define SIZEOFARRAY(a) (sizeof(a)/sizeof (a[0]))
int main (void)
{
	int numbers [5]={1,2,3,4,5};
	printf ("%ld\n",SIZEOFARRAY(numbers));
	int num []={1,2,3};
	printf ("%ld\n",SIZEOFARRAY(num));
	char letters[] = {'a','b','c'};
	char let [] = "abc";
	printf ("%ld\n",SIZEOFARRAY (letters));
	printf ("%ld\n",SIZEOFARRAY (let));
	return 0;
}
