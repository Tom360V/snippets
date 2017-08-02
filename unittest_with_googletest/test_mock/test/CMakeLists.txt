cmake_minimum_required(VERSION 2.8.4)

# ENTER [PROJECT NAME] HERE
project (Test_myApp)

#Enable test functionality
enable_testing()

#Flags

#-Dgtest_disable_pthreads=ON

SET(CMAKE_BUILD_TYPE debug)
SET(CMAKE_CXX_FLAGS_DEBUG -fno-delete-null-pointer-checks)
SET(CMAKE_CXX_FLAGS_DEBUG "-O0 -g" )
 
message("CMAKE_CXX_FLAGS_DEBUG  : ${CMAKE_CXX_FLAGS_DEBUG}")
message("CMAKE_CXX_FLAGS        : ${CMAKE_CXX_FLAGS}")



# Add google test directory so we can use the testframework
set(GTEST_DIR /usr/lib/googletest)
include_directories( ../inc ${GTEST_DIR}/googletest/include/)


#Specified directories will be searched for CMakeList.txt,
# if that file exist, it will be executed as part of this project!
add_subdirectory(${GTEST_DIR} ./gtest)  # add test environment
add_subdirectory(../ MUT)               # Add Module Under Test


#create executable
# ENTER [TEST NAME] and [SOURCE FILES]
add_executable(test_myApp test_app.cpp MOCK_storeLastValue.cpp)


# ENTER[TEST NAME], [APPLICATION NAME, same as in CMakeList.txt in application directory]
# and gmock_main for the testframework
target_link_libraries (test_myApp myApp pthread gmock_main)


# ENTER [PROJECT NAME] and [TEST NAME]
add_test(TEST_myApp test_myApp)
