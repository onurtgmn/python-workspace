#include <stdio.h>
int fibonacci (int);
int main (void)
{
	printf ("Fibonacci sequences 1 1 2 3 5 8 .... \n");
	printf ("Please enter the term number : ");
	int number ;
	scanf("%d",&number);
	printf ("%d\n",fibonacci (number));
	return 0;



}
int fibonacci (int number)
{
	if (number == 1 || number == 2)
	
	{
		return 1;
	
	}
	else 
	{
		return fibonacci(number-1)+fibonacci(number-2);
	
	}


}
