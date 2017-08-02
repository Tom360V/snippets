//#include <stdio>
//#include <stdlib.h>
//#include <check.h>
//#include <string.h>

#include "app.h"
#include <gtest/gtest.h>
#include "MOCK_storeLastValue.h"

using ::testing::_;
using ::testing::Return;

#define PRINTF(x)
//#define PRINTF(msg) printf(msg);

/******************************************************************************
 * FIXTURES
 *****************************************************************************/
class TEST_app_FIXTURE : public ::testing::Test
{
    protected:
    virtual void SetUp()
    {
        PRINTF("\n*** SetUp ***");

        //Set expectations
        MOCK_storeLastValue MOCK;
        EXPECT_CALL(MOCK, StoreLastValue_init()).Times(1);

        //Call function
        app_init();
    }

    virtual void TearDown()
    {
        PRINTF("\n*** TearDown ***");
    }
};
/******************************************************************************
 * TESTS
 *****************************************************************************/

/*
 * Description: Check if init initialized the local variable
 */
TEST_F(TEST_app_FIXTURE, init)
{
    MOCK_storeLastValue MOCK;

    EXPECT_CALL(MOCK, StoreLastValue_init()).Times(1);
    app_init();

    EXPECT_CALL(MOCK, StoreLastValue_get()).Times(1);
    ASSERT_EQ(0, app_get());
}

/*
 * Description: Check if the set function works
 */
TEST_F(TEST_app_FIXTURE, set)
{
    MOCK_storeLastValue MOCK;

    //Set expectation
    EXPECT_CALL(MOCK, StoreLastValue_set(5)).Times(1);

    //Call FUT
    app_set(5);
}

/*
 * Description: Check if the set function only remembers the last set value
 */
TEST_F(TEST_app_FIXTURE, get)
{
    MOCK_storeLastValue MOCK;

    //Set expectations
    EXPECT_CALL(MOCK, StoreLastValue_set(5)).Times(1);
    EXPECT_CALL(MOCK, StoreLastValue_set(6)).Times(1);
    EXPECT_CALL(MOCK, StoreLastValue_set(7)).Times(1);
    EXPECT_CALL(MOCK, StoreLastValue_get()) .Times(1)
                                            .WillOnce(Return(7));

    //Set test sequence
    app_set(5);
    app_set(6);
    app_set(7);

    //Check return value
    ASSERT_EQ(7, app_get());
}

/******************************************************************************
 *  MAIN FUNCTION
 */
int main(int argc, char **argv)
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
