#include <stdio.h>
int main (void)
{
	char c= '1';
	printf ("first:%d",sizeof(c));
	int i= (int)c;
	printf ("Size :%d\n",sizeof(i));
	printf ("%d\n",i);
}
