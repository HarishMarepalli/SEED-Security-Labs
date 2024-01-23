/*
In this example of a buffer overflow, we attempt to bypass the assignment statement by calling a method named "function" from the main function. When the method is called, the parameters are stored on the stack along with the return address, saved frame pointer, and local variables like buffer1 and buffer2, which are also pushed onto the stack.
*/

#include<stdio.h>

void function (int a, int b, int c)
{
	char buffer1[5];
	char buffer2[10];
}

void main()
{
	int x;
	x = 0;
	function(1,2,3);
	x = 1;	//Bypass the assignment statement 'x = 1' by lauching the attack
	printf("%d\n",x);
}
