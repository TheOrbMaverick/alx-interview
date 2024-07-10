# FACTORIAL

'''
My notes.
I need to find out all the complexities (Big O notations) of every code I write in this file.
'''
# Iterative factorial
def iterative_factorial(n):
    # This is what factorial of 5 looks like:
    #   (5 * 4 * 3 * 2 * 1)
    #   The result of which is 120
    # assign a default value to factorial that's greater than 0
    fact = 1

    # for the range starting from 2 to the point where n+1
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
        temp *= n
    return temp

print(recursive_factorial(4))


# PERMUTATION


# PASCAL'S TRIANGLE

# Iterative solution
def pascals_triangle(row_num):

    if row_num <= 0:
        return []
    
    triangle = [[1]]

    for _ in range(1, row_num):
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i-1] + prev_row[i])

        new_row.append(1)
        triangle.append(new_row)

    return triangle

print(pascals_triangle(5))


# Recursive solution
def pascals_recursive_triangle(row_num):

    if row_num <= 0:
        return []
    

