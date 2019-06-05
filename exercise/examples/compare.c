#include<stdio.h>
int result = 1;
float absolute (float value)
{
	if (value < 0)
	{
		value = -value;
	}
	return value;
}
int checkEquality(float a,float b)
{

	if (absolute(a-b)>0.000001)
	{
		result = 0;
	}
	return result;

}
int main (void)
{
	float a;
	float b;
	scanf ("%f",&a);
	scanf ("%f",&b);
	printf ("*****************************************\n");
	printf ("Comparing two number by using epsilon value...\n");
	printf ("If two numbers are equal,the result is 1;otherwise it is 0...\n");
	printf ("*****************************************\n");
	printf ("The result is %d...\n",checkEquality(a,b));
	return 0;



}
