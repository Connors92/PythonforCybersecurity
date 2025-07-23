#!/usr/bin/env python3
# Created by Connor Gronsky on 7/23/2025

number = int(input("Enter a number: "))
is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(str(number) + " is prime")
else:
    print(str(number) + " is NOT prime")
