def solution(num):  # we are going to reverse a string and so take in a num as a parameter
    string = str(num)  # we convert the num to a string to deal with the - sign

    if string[0] == '-':  # if the first char is a - sign, then
        # we will return the negative sign + the converted integer, stepping backwards with slice
        return int('-' + string[:0:-1])
    else:
        # if a positive number, we'll use slice to step backwards through it
        return int(string[::-1])


print(solution(-231))
print(solution(532))
