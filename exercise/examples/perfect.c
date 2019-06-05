#include <stdio.h>
int main (void)
{
	int result = 0 ;
	int number ;
	scanf ("%d",&number);
	int i = 1;
	while (i<number)
	{
		if (number % i == 0)
		{
			result +=i;
		}
		i++;
	}
	if (result == number)
	{
		printf ("%d is a perfect number...\n",number);
	}
	else 
	{
		printf ("%d is not a perfect number...\n",number);
	}
	return 0;

}
