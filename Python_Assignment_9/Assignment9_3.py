# Create a Python program that uses multiprocessing.Pool to compute factorial of numbers in a list.

import multiprocessing

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def main():
    numbers = [5, 7, 10, 12]  # List of numbers

    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)

    for n, r in zip(numbers, results):
        print(f"Factorial of {n} is {r}")

if __name__ == "__main__":
    main()
