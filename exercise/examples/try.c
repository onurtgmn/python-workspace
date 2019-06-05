#include <stdio.h>
int sum(int ,int);
int addw(int ,int);
int main (void)
{
	printf ("%d\n",addw(sum(2,3),9));
	return 0;

}
int sum(int x,int y)
{

	return x+y;
}
int addw(sum(int x,int y),int w)
{
	return w+sum(x,y);

}
