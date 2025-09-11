#include "include/print.h"

int main()
{
    print();
    print("Hello world");
    int a = 5;
    int b = 6;
    int c = 20;
    print("a =", a, "b =", b, "c =", c);

    for(int i = 0; i < 10; i++)
    {
        print("i =", i);
    }


    return 0;
}