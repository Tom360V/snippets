#ifndef ENDIANNESS_H
#define ENDIANNESS_H

#include <limits.h>
#include <stdint.h>

/*  Endianness representation of 4A3B2C1D on memoryaddress 10
 *
 *  address | 10 | 11 | 12 | 13
 *  --------+----+----+----+----
 *  BIG     | 4A | 3B | 2C | 1D
 *  LITTLE  | 1D | 2C | 3B | 4A
*/

#define WE_ARE_BIG_ENDIAN (!*(unsigned char *)&(uint16_t){1})


#define SWAP16(a)   ((a<<8)&0xff00) |   \
                    ((a>>8)&0x00ff)    
                
#define SWAP32(a)   ((a>>24)&0x000000ff) |  \
                    ((a<< 8)&0x00ff0000) |  \
                    ((a>> 8)&0x0000ff00) |  \
                    ((a<<24)&0xff000000)

#define SWAP_int8_t  (a) a  //Do nothing!
#define SWAP_uint8_t (a) a  //Do nothing!
#define SWAP_int16_t (a)    SWAP16(a)
#define SWAP_uint16_t(a)    SWAP16(a)
#define SWAP_int32_t (a)    SWAP32(a)
#define SWAP_uint32_t(a)    SWAP32(a)

#define SWAP2BIG(var, type)         \
({                                  \
    if(!WE_ARE_BIG_ENDIAN)          \
    {                               \
        var = SWAP_ ## type (var);  \
    }                               \
    (var);                          \
})                                  \

#define SWAP2LITTLE(var, type)      \
({                                  \
    if(WE_ARE_BIG_ENDIAN)           \
    {                               \
        var = SWAP_ ## type (var);  \
    }                               \
    (var);                          \
})                                  \
    

#endif  /*ENDIANNESS*/
