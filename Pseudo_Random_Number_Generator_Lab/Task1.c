//Generate Encryption Key in a Wrong Way
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define KEYSIZE 16
void main()
{
	printf("CMPE209-Assignment3-016707314-Pseudo Random Number Generator - Task1- Generate Encryption Key in a Wrong Way\n");
	int i;
	char key[KEYSIZE];
	printf("%lld\n", (long long) time(NULL));
	//srand (time(NULL));
	for (i = 0; i< KEYSIZE; i++){
		key[i] = rand()%256;
		printf("%.2x", (unsigned char)key[i]);
	}
	printf("\n");
}
