g++ -c -fPIC .\Utils\Clibs\fib\fib.cpp -O2 -o .\Utils\Clibs\fib\fib.o
g++ -shared -Wl,-soname,.\Utils\Clibs\fib\libfib.so -o .\Utils\Clibs\fib\libfib.so  .\Utils\Clibs\fib\fib.o