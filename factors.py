#!/usr/bin/python3
import sys


def factorise(num):
    """Factorise a number into two factors
    Args:
            num: number to be factorised
    Returns:
            fact1: One of the factors
    """
    fact1 = 2
    while num % fact1:
        fact1 += 1
    return fact1


def main():
    """Entry point
    Returns:
            None
    """
    file_name = "test.txt"
    file = open(file_name, "r")
    num_list = file.readlines()

    for num in num_list:
        fact1 = factorise(int(num.rstrip('\n')))
        fact2 = int(num) // fact1
        print("{} = {} * {}".format(num.rstrip('\n'), fact1, fact2))


if __name__ == "__main__":
    main()
