#!/usr/bin/env python3
import types, sys

def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

def main():
    # checking if fib is a generator
    if type(fib()) == types.GeneratorType:
        try:
            number = int(sys.argv[1])
        except:
            print("you didn't give valid input!")
            exit()
        print("Generating", sys.argv[1], "numbers in Fibonacci series...")
        counter = 0
        for number in fib():
            print(number)
            counter += 1
            if counter == int(sys.argv[1]):
                break
        
        
if __name__ == "__main__":
    main()