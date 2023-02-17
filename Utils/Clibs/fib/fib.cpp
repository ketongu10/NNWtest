#include <iostream>

class Fib{
    public:
        void bar(){
            std::cout << "Hello" << std::endl;
        }
        int fib(int n) {
            if (n<=1) {
                return 1;
            } else {
                return fib(n-1)+fib(n-2);
            }
        }
};

extern "C" {
    Fib* Fib_new(){ return new Fib(); }
    void Fib_bar(Fib* foo){ foo->bar(); }
    int Fib_fib(Fib* foo, int n) {return foo->fib(n);}
}