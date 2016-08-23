#include <stdio.h>


int factorial(int n)
{
    return n == 0 ? 1 : n * factorial(n-1);
}


int main()
{
    for (int i=0; i<10; ++i)
    {
        printf("Factorial of %d = %d\n", i, factorial(i));
    }
}
