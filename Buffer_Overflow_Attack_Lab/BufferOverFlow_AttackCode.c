/*
In this example of a buffer overflow, we attempt to bypass the assignment statement by calling a method named "function" from the main function. When the method is called, the parameters are stored on the stack along with the return address, saved frame pointer, and local variables like buffer1 and buffer2, which are also pushed onto the stack.

In this scenario, our aim is to modify the return address of the function by increasing its value by 8 bytes. By doing so, we can bypass the assignment statement immediately following it and proceed directly to the printf statement located at the end.
*/

#include<stdio.h>

void function (int a, int b, int c)
{
	char buffer1[5];
	char buffer2[10];
	
	int *ret;
	
	/*
	Immediately preceding the buffer1[] array on the stack, there is the Saved Frame Pointer (SFP), and before that, the return 		address. The return address is located 4 bytes beyond the end of buffer1[]. However, it is essential to note that buffer1[] is 	 actually 2 words in length, equivalent to 8 bytes. As a result, the address calculated is 12 bytes from the start of buffer1[]. 		Consequently, in the given statement, the value of buffer1 is incremented by 12.
	*/
	ret = buffer1 + 12;
	
	/*
	To determine the specific value of 8 bytes that needed to be added in this scenario, we utilized a debugger tool such as "gdb". 		By employing gdb, we examined the program's execution and stack layout to identify the correct number of bytes required for our 		intended manipulation. Through this process of debugging and analysis, we verified and established the value of 8 bytes as the 	 necessary adjustment in this particular case.
	*/
	(*ret) += 8;
}

void main()
{
	int x;
	x = 0;
	function(1,2,3);
	x = 1;	//Bypass the assignment statement 'x = 1' by lauching the attack
	printf("%d\n",x);
}
