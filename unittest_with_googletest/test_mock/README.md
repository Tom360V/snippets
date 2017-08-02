# Unittest with google test
source: https://github.com/google/googletest

## configure googletest:
    $ cd /usr/lib
    $ git clone https://github.com/google/googletest
    edit: /usr/lib/googletest/googletest/CMakeList.txt:
    change OFF to ON in this row:
        option(gtest_disable_pthreads "Disable uses of pthreads in gtest." OFF)


## build lib:
    $ mkdir bld
    $ cd bld
    $ cmake ..
    $ make


## Create mockfiles
  use genMock.py to generate the mock
  src: https://github.com/Tom360V/snippets/blob/master/python%20generate%20mockfile%20for%20GTEST/genMock.py
  copy genMock.py to the test directory
  $ python genMock.py ../inc/storeLastValue.h


## build test
first: make sure that test/CMakeList.txt the correct path to googletest checkout is configured:
search for "set(GTEST_DIR /usr/lib/googletest)" and check the path!

    $ cd test
    $ mkdir bld
    $ cd bld
    $ cmake ..
    $ make
    $ make test
    or
    $ ctest         (same as 'make test')
    or
    $ ctest -VV     (verbose)
    
    Note: if ctest -VV reports in black/with add "export GTEST_COLOR=1" to you ".bashrc"
