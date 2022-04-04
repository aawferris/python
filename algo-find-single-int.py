# sets up the driver code
ar = [7, 3, 5, 4, 5, 3, 4]
# we'll take the length of the array for iteration in the function
n = len(ar)


def findSingleNumber(ar, n):  # the function takes in the array and the length of the array
    res = 0  # sets the initial result to zero

    for i in range(n):  # the for loop iterates n times (length of the array)
        # this uses XOR (exclusive or) which is a comparison operator - it breaks each int into bits and then compares the bits
        res ^= ar[i]
    return res  # returns the result and breaks out of the lop


# here we print the result, by calling the method and passing in parameters
print(findSingleNumber(ar, n))
