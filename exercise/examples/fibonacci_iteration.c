#include <stdio.h>
int fibonacci(int);
int main (void)
{
	printf ("**********************\n");
	printf ("Fibonacci Computing Program ....\n");
	printf ("Please enter the term number : ");
	int term ;
	scanf ("%d",&term);
	printf ("%d\n",fibonacci(term));
	printf ("**********************\n");
	return 0;


}
int fibonacci (int term)

{
	int a = 1 ;
	int b = 1 ;
	int i = 2 ;
	int temp ;
	while (i<term)
	{
		temp = a;
		a = b;
		b = temp+b;
		i++;
	
	
	}
	return b;



}
