# Unittest with check
check: https://libcheck.github.io/check/

## build lib:
    $ mkdir bld
    $ cd bld
    $ cmake ..
    $ make

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