/*
 * app.c
 *
 * Created: 31-07-2017
 *  Author: tkoene
 */

#include <string.h>
#include "app.h"

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

void app_init()
{
    myValue = 1;
}

int8_t app_get()
{
    return myValue;
}

void app_set(int8_t newValue)
{
    myValue = newValue;
}