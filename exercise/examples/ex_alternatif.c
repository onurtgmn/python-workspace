#include <stdio.h>
int find_summation(int,int);
int main (void)
{
	int from = 7 ;
	int to = 7 ;
	while (to < 100)
	{
		if (find_summation (from,to)==279)
		{
			printf ("%d\n",to);
		}
		to++;
	}
	
	return 0;

}

int find_summation (int from ,int to)
{
	int result = 0 ;
	result = (from *(from-1))/2;
	int temp = 0 ;
	temp = (to*(to+1))/2;
	int answer = temp - result;
	return answer;



}
