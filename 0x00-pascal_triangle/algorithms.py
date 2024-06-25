# FACTORIAL

# Iterative factorial
def iterative_factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

print(iterative_factorial(5))


# Rcursive factorial
def recursive_factorial(n):
    if n == 1:
        return n
    else:
        temp = recursive_factorial(n-1)
        print(temp, n)
        temp *= n
    return temp

print(recursive_factorial(5))


# PERMUTATION