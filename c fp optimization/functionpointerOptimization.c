/*
 * CONTEXT FOR THIS EXPERIMENT:
 * does the compiler optimize functionpointers?
 *
 * uncomment #define USE_FUNCTION_POINTER and compile this file
 *   $ gcc fpStructSize.c -o a1.exe
 *
 * comment out #define USE_FUNCTION_POINTER and compile this file
 *   $ gcc fpStructSize.c -o a2.exe
 *
 * check this size of both files:
 *   $ size a1.exe
 *      text    data     bss     dec     hex filename
 *     37020    1748    2608   41376    a1a0 x.exe
 *
 *   $ size a2.exe
 *      text    data     bss     dec     hex filename
 *     37020    1748    2608   41376    a1a0 z.exe
 *
 * Both files have the same size... interresting?
 * complete table is optimized?
 */
 
#include <stdio.h>

//#define USE_FUNCTION_POINTER

#ifdef USE_FUNCTION_POINTER
    #define MY_TEXT             "using function pointer\r\n"
#else
    #define MY_TEXT             "NOT!!!function pointer\r\n"
#endif

/******************************************************************************
 * Functions required for the test
 *****************************************************************************/
void function1()
{
    printf("function1\r\n");
    printf(MY_TEXT);
}

void function2()
{
    printf("function2\r\n");
    printf(MY_TEXT);
}

/******************************************************************************
 * Create table, ONLY enabled when this USE_FUNCTION_POINTER is defined/uncommented!
 *****************************************************************************/
#ifdef USE_FUNCTION_POINTER
typedef void (*func_t)();

typedef const struct
{
    func_t fpFunction1;
    func_t fpFunction2;
} functionTable_t;

functionTable_t fTable =
{
    &function1,
    &function2,
};
#endif

/******************************************************************************
 * Main
 *****************************************************************************/
int main(int argc, char **argv)
{
#ifdef USE_FUNCTION_POINTER
    fTable.fpFunction1();
    fTable.fpFunction2();
#else
    function1();
    function2();
#endif
    return 0;
}
