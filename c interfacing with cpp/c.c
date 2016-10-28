#include <stdint.h>
#include <stdio.h>
#include "c2cpp.h"

int main(void)
{
	int x;
    printf("\nhello world!");
    setValue(4);
    setValue(5);
    x = getValue();
    printf("\nValue: %d",x);
	return 0;
}