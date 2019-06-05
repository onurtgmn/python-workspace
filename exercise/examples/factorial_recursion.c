#include <stdio.h>
int factorial (int );
int main (void)
{
	int number ;
	printf ("Enter the number : ");
	scanf("%d",&number);
	printf ("%d\n",factorial (number));
	return 0;



}
int factorial (int number)
{
	if (number == 0)
	{
		return 1;
	}
	else 
	{
		return number* factorial (number-1);
	}

}
