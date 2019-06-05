#include <stdio.h>
int absolute(int);
int main (void)
{	
	while (1)
	{
		char value ;
		scanf ("%c",&value);
		if (value == 'q')
		{
			printf ("Exiting program ...\n");
			break;
		}
		int temp = (int)value;
		printf ("Temp:%d\n",temp);
		printf ("%d\n",absolute (temp));
		return 0;

	
	}	
}
int absolute (int value)
{
	if (value<0)
	{
		value = -value;
	}
	return value;
}
