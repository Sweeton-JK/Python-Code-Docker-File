def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    num = int(input("Enter a number to calculate its factorial: "))
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
