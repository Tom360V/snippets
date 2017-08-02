/*
 * storeLastValue.h
 *
 * Created: 31-07-2017
 *  Author: tkoene
 */

/******************************************************************************
 * DEFINES
 *****************************************************************************/

/******************************************************************************
 * PUBLIC TYPES AND ENUMS
 *****************************************************************************/

/******************************************************************************
 * PUBLIC FUNCTIONS
 *****************************************************************************/

#ifndef STORE_LAST_VALUE_H_
#define STORE_LAST_VALUE_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

void    StoreLastValue_init(void);
int8_t  StoreLastValue_get(void);
void    StoreLastValue_set(int8_t newValue);

#ifdef __cplusplus
}
#endif

#endif /* STORE_LAST_VALUE_H_ */
