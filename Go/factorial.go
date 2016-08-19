package main

import "fmt"


func factorial (i int) int {
    if i == 0 {
        return 1

    } else {
        return i*factorial (i-1);
    }
}


func main() {
    for i := 0; i<10; i++ {
        fmt.Println(factorial(i));
    }
}
