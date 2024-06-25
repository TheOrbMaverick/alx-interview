#PASCAL'S TRIANGLE

# - 1 is always at the top
# - 1,1 is always on the second row
# - the next 3 


def pascal_triangle(n):
    # If the number of rows is less than 1
    if n <= 0:
        return []
    
    # Initialize the first row. Triangle is an array of arrays
    triangle = [[1]]

    # Check for the number of rows required starting from 1
    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        # Loop through the for loop
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i-1] + prev_row[i])
        
        new_row.append(1)
        triangle.append(new_row)
    
    return triangle