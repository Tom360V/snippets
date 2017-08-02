//#include <stdio>
//#include <stdlib.h>
//#include <check.h>
//#include <string.h>

#include "app.h"
#include <gtest/gtest.h>

/******************************************************************************
 * SETUPs
 *****************************************************************************/
void setup(void)
{
    app_init();
}

void setup_another(void)
{
    app_init();
    app_set(2);
}

/******************************************************************************
 * TEARDOWNs
 *****************************************************************************/
class TEST_app_FIXTURE : public ::testing::Test
{
     protected:
     virtual void SetUp()
     {
         app_init();
     }

     virtual void TearDown()
     {
     }
};
/******************************************************************************
 * TESTS
 *****************************************************************************/

/*
 * Description: Check if init initialized the local variable
 * NOTE: the Setup() function will NOT be called, so the module is NOT "initialized"
 */
TEST(TEST_app, initWith_NO_Fixture)
{
    ASSERT_EQ(0, app_get());
}

/*
 * Description: Check if init initialized the local variable
 * NOTE: the SetUp() function will is called and therefore the module is in a defined state!
 */
TEST_F(TEST_app_FIXTURE, initWithFixture)
{
    ASSERT_EQ(1, app_get());
}

/*
 * Description: Check if the set function works
 */
TEST_F(TEST_app_FIXTURE, set)
{
    app_set(5);
    ASSERT_EQ(5, app_get());
}

/*
 * Description: Check if the set function only remembers the last set value
 */
TEST_F(TEST_app_FIXTURE, set_2)
{
    ASSERT_EQ(1, app_get());
    app_set(5);
    app_set(6);
    app_set(7);
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