cmake_minimum_required(VERSION 2.8.4)
project (myApp)

#Add include directories
include_directories("inc")

#Add sources
set(srcs src/app.c)             #TKE: note that "src/storeLastValue.c" is NOT included!!!!
                                # This is on purpose: to prove that we can build a library with dependencies
                                # without linking to the dependencies!
                                # If we use this library, somehow we should provide the required dependencies,
                                #  check the CMakeList.txt in the test directory.
                                

#Add Library
add_library(myApp ${srcs})
