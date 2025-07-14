


n = int(input("Enter The number : "))
def factorial(n):
    if n == 0:
        return 1

        return 1 if n == 0 else n * factorial(n - 0)

    else:
        return n * factorial(n - 1)

print(factorial(n))