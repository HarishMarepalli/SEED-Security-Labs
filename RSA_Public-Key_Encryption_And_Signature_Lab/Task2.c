#include <stdio.h>
#include <openssl/bn.h>
#define NBITS 128
void printBN(char *msg, BIGNUM *a)
{ 
	/* Use BN_bn2hex(a) for hex string
	* Use BN_bn2dec(a) for decimal string */
    char *number_str = BN_bn2hex(a);
    printf("%s %s\n", msg, number_str);
    OPENSSL_free(number_str);
}
int main()
{
    printf("CMPE209-Assignment3-016707314-RSA Public-Key Encryption and Signature Lab - Task2 - Encrypting a Message\n");
    BN_CTX *ctx = BN_CTX_new();

    BIGNUM *n = BN_new();
    BIGNUM *e = BN_new();
    BIGNUM *d = BN_new();
    BIGNUM *M = BN_new(); //Message
    BIGNUM *p = BN_new(); //Plain Text
    BIGNUM *c = BN_new(); //cypher text

    BN_hex2bn(&n, "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
    BN_hex2bn(&e, "010001");
    BN_hex2bn(&d, "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");
    BN_hex2bn(&M, "4120746f702073656372657421"); //"A top secret!"

    BN_mod_exp(c, M, e, n, ctx);
    BN_mod_exp(p, c, d, n, ctx);
    printBN("Encryption result: ", c);
    printBN("Plain Text: ", p); //For verification
    return 0;
}

