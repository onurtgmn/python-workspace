#include <stdio.h>
int main (void)
{
	int result = 0 ;
	int i = 7;
	int key = 1;
	while (key)
	{
		while (i<100)
		{
			result += i;
			if (result == 255)
			{
				printf("%d\n",i);
				key=0;
			}
			i++;
		}
	}
	return 0;
}
