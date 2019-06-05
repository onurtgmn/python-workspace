#include <stdio.h>
int IsPrime (int number);
int main (void)
{
	printf ("*********************\n");
	printf ("Is This Number Prime ?\n");
	printf ("*********************\n");
	int number ;
	printf ("Enter the number :");
	scanf ("%d",&number);
	if (number == 0 || number == 1)
	{
		printf ("%d is not a prime number...\n",number);
	}
	else
	{
		if(IsPrime(number)==1)
		{
			printf ("%d is a prime number...\n",number);
		}
		else 
		{
			printf ("%d is not a prime number...\n",number);
		}
	}

}
int IsPrime (int number)
{
	int i= 2;
	while (i < number)
	{
		if (number % i == 0)
		{
			return 0;
		}
		else 
		{
			return 1;
			
		}
		i++;
	
	}

}
