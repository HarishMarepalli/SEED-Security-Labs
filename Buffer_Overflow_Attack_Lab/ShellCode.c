/*
A shellcode is basically a piece of code that launches a shell. If we use the C code to implement it, it will look like the following code. This is the code to spawn a shell in C.
*/
#include <stdio.h>

void main()
{
	char *name[2];
	
	name[0] = "/bin/sh";
	name[1] = NULL;
	execve(name[0], name, NULL);
}
