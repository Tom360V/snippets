#include "stdio.h"
#include "endianness.h"


void main(void)
{
    uint16_t big16    = 0x1122;
    uint16_t little16 = 0x1122;
    SWAP2BIG(big16, uint16_t);
    SWAP2LITTLE(little16, uint16_t);
    printf("\nuint16_t 0x%04X", big16);
    printf("\nuint16_t 0x%04X", little16);

    uint32_t big32    = 0x11223344;
    uint32_t little32 = 0x11223344;
    SWAP2BIG(big32, uint32_t);
    SWAP2LITTLE(little32, uint32_t);
    printf("\nuint32_t 0x%04X", big32);
    printf("\nuint32_t 0x%04X", little32);
}
