cmake_minimum_required(VERSION 2.8.4)
project (app)

#Add include directories
include_directories("inc")

#Add sources
set(srcs src/app.c)

#Add Library
add_library(app STATIC ${srcs})
