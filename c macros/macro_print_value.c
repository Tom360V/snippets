/*
 * BUILD WITH :gcc macro_print_value.c -o x.exe; ./x.exe
 */
 
#include <stdio.h>

#define VALUE(x,...)        #x
#define _STR(str, ...)      VALUE(str)

#define PRINT_1			print this
#define PRINT_2			"hello world"
#define PRINT_3			123

#pragma message "PRINT MACRO: " _STR(PRINT_1)
#pragma message "PRINT MACRO: " _STR(PRINT_2)
#pragma message "PRINT MACRO: " _STR(PRINT_3)


int main( int argc, const char* argv[])
{
    printf("%s\r\n", _STR(PRINT_1));
    printf("%s\r\n", PRINT_2);
    printf("%d\r\n", PRINT_3);
    return 0;
}