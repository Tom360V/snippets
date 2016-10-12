/*
 * BUILD WITH :gcc macro_build_functiontable.c -o x.exe; ./x.exe
 */
 
#include <stdio.h>
#include <stdint.h>

/******************************************************************************
 * DEFINES
 *****************************************************************************/
 
#define CMD_CAT(a, b)                               a ## b

#define CMD_ADD_0(...)          
#define CMD_ADD_1(cmd, args, func, descr, ...)      {cmd, args, func, descr },
#define CMD_ADD(a)                                  CMD_CAT(CMD_ADD_, a)(a ## _CMD, a ## _ARGS, a ## _FUNC, a ## _DESC)

//#define CMD_PREFIX_0(name, ...)                     __attribute__((unused)) static uint8_t
#define CMD_PREFIX_0(name, ...)                     static uint8_t
#define CMD_PREFIX_1(name, ...)                     static uint8_t
#define CMD_PREFIX(name)                            CMD_CAT(CMD_PREFIX_, name)(name ## _FUNC)

#define CMD_GEN_FUNC_0(name)                        __attribute__((unused)) static uint8_t name(char *msgId, uint8_t *msgArgs, int8_t nofArgs);
#define CMD_GEN_FUNC_1(name)                        static uint8_t name(char *msgId, uint8_t *msgArgs, int8_t nofArgs);
#define CMD_GEN_FUNC(x, name)                       CMD_CAT(CMD_GEN_FUNC_, x)(name)

/******************************************************************************
 * COMMAND SET
 *
 * add YOUR commands below!
 *
 *****************************************************************************/
#define CMD_SDS         1
#define CMD_SDS_CMD     "sds"
#define CMD_SDS_DESC    "Set Device Specifications"
#define CMD_SDS_ARGS    4
#define CMD_SDS_FUNC    cmd_function_sds
CMD_PREFIX(CMD_SDS)     cmd_function_sds(char *msgId, uint8_t *msgArgs, int8_t nofArgs);

#define CMD_CAP         0
#define CMD_CAP_CMD     "CAP"
#define CMD_CAP_DESC    "Get list of system capabilities."
#define CMD_CAP_ARGS    1
#define CMD_CAP_FUNC    cmd_function_Capabilities
CMD_PREFIX(CMD_CAP)     cmd_function_Capabilities(char *msgId, uint8_t *msgArgs, int8_t nofArgs);
//OR More beautiful solution:
//CMD_GEN_FUNC(CMD_CAP, cmd_function_Capabilities)
    //But, some IDE's you can't use "Goto Implementation" / "(ALT-G)" anymore if you use this macro.


#define VALUE4(x,...)       #x
#define VALUE3(x,...)       #x  VALUE4(__VA_ARGS__)
#define VALUE2(x,...)       #x  VALUE3(__VA_ARGS__)
#define VALUE(x,...)        #x  VALUE2(__VA_ARGS__)
#define _STR(str, ...)      VALUE(str)
#define _FUNC(a,...)        VALUE(a)
#pragma message "PRINT MACRO: " _STR(CMD_ADD(CMD_SDS))
#pragma message "PRINT MACRO: " _STR(CMD_ADD(CMD_CAP))


/******************************************************************************
 * CREATE TABLE
 *
 * add YOUR commands below!
 *
 *****************************************************************************/
typedef uint8_t (* CMD_ACTION_FP)(char *msgId, uint8_t *msgArgs, int8_t nofArgs);

typedef struct
{
    char             *msgID;          // Specification for the message
    uint8_t           args;           // Specification for the message
    CMD_ACTION_FP     pActionFn;      // Pointer to function to actually handle the message
    char             *pDescription;   // Short description for commandline
} CMD_TABLE_ENTRY_T;

static const CMD_TABLE_ENTRY_T cmdTable[]=
{
    // Serial Debug Core command set
    CMD_ADD(CMD_SDS)
    CMD_ADD(CMD_CAP)
};

/******************************************************************************
 * COMMAND FUNCTION IMPLEMENTATIONS
 *
 *****************************************************************************/
static uint8_t cmd_function_sds(char *msgId, uint8_t *msgArgs, int8_t nofArgs)
{
    printf("   cmd_function_sds\r\n");
    uint8_t idx;
    for(idx=0; idx<nofArgs; idx++)
    {
        printf("      - %d\r\n",msgArgs[idx]);
    }
    return 0;
}

static uint8_t cmd_function_Capabilities(char *msgId, uint8_t *msgArgs, int8_t nofArgs)
{
    printf("   cmd_function_Capabilities\r\n");
    uint8_t idx;
    for(idx=0; idx<nofArgs; idx++)
    {
        printf("      - %d\r\n",msgArgs[idx]);
    }
    return 0;
}



/******************************************************************************
 * MAIN
 *****************************************************************************/
int main(int argc, const char* argv[])
{
    CMD_ACTION_FP pFunction;
    uint8_t result;
    uint8_t idx;
    uint8_t nofEntries = sizeof(cmdTable) / (sizeof(cmdTable[0]));
    uint8_t args[] = {1,2,3,4,5,6,7,8};

    printf("nof entries in table: %d\r\n", nofEntries);

    for(idx=0; idx<nofEntries; idx++)
    {
        pFunction = cmdTable[idx].pActionFn;
        if(NULL != pFunction)
        {
            printf("-execute function: %d\r\n", idx);
            result = pFunction(cmdTable[idx].msgID, args , cmdTable[idx].args);
        }
        else
        {
            printf("-skip function: %d\r\n", idx);
        }
    }       
    return 0;
}
