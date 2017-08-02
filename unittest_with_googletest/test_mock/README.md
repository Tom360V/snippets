# Unittest with check
check: https://libcheck.github.io/check/

## build lib:
    $ mkdir bld
    $ cd bld
    $ cmake ..
    $ make


##Create mockfiles
  use genMock.py to generate the mock
  src: https://github.com/Tom360V/snippets/blob/master/python%20generate%20mockfile%20for%20GTEST/genMock.py
  copy genMock.py to the test directory
  $ python genMock.py ../inc/storeLastValue.h


## build test
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