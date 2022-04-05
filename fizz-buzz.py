
for i in range(1, 101):  # setting up the range this way eliminates the zero and makes sure 100 is counted
    print(i+1)  # this will just print indices increasing by 1
    if i % 3 == 0 and i % 5 == 0:  # do both first since it is the most specific case.  Use % operator == 0 to see if there is a remainder
        # we print the stringified index and FizzBuzz
        print(str(i) + ' is a multiple of 5 and 3.  FizzBuzz!')
    elif i % 3 == 0:  # handles only mult of 3
        print(str(i) + ' is a multiple of 3. Fizz!')
    elif i % 5 == 0:  # handles only mult. of 5
        print(str(i) + ' is a multiple of 5.  Buzz!')
    else:  # if not a multiple, just print the number
        print(str(i))
