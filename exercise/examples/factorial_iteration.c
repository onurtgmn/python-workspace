#include <stdio.h>
int factorial(int );
int main (void)
{
	int number ;
	printf ("Enter the number :");
	scanf ("%d",&number);
	printf ("%d\n",factorial(number));
	return 0;

}
int factorial (int number)
{
	int result = 1;
	while (number > 0)
	{
		result *= number;
		number --;
		
	}
	return result ;


}
