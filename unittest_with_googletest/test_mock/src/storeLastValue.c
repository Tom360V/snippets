/*
 * storeLastValue.c
 *
 * Created: 31-07-2017
 *  Author: tkoene
 */

#include <string.h>
#include "storeLastValue.h"

/******************************************************************************
 * DEFINES
 *****************************************************************************/

/******************************************************************************
 * PRIVATE TYPES AND ENUMS
 *****************************************************************************/

/******************************************************************************
 * PRIVATE VARIABLES
 *****************************************************************************/
static int8_t myValue = 0;

/******************************************************************************
 * PRIVATE FUNCTIONS PROTOTYPES
 *****************************************************************************/

/******************************************************************************
 * PRIVATE FUNCTIONS
 *****************************************************************************/

/******************************************************************************
 * PUBLIC FUNCTIONS
 *****************************************************************************/

void StoreLastValue_init()
{
    myValue = 1;
}

int8_t StoreLastValue_get()
{
    return myValue;
}

void StoreLastValue_set(int8_t newValue)
{
    myValue = newValue;
}
