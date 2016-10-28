#include "c2cpp.h"
#include "cpp.h"

myClass myC;

void setValue(int newValue)
{
	myC.setValue(newValue);
}

int getValue()
{
	return myC.getValue();
}

