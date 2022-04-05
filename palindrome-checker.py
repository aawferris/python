
def isPalindrome(s):  # This function takes in 's' as a parameter
    # this will return when s is equal to the reverse of s (here, we're using the slice tool which uses the syntax ; start, stop, step -- so we're not defining start and stop but telling it to step backwards through the string)
    # so again, this is common syntax to reverse a string - when left blank, it defaults to '1'
    return s == s[::-1]


s = "racecar"
# we're saving the function as a variable to be able to use it below
ans = isPalindrome(s)

if ans:
    print("Yes, this is a palindrome")
else:
    print("No, this is not a palindrome")


# Another way - this is the way my brain was working it out
string = "aIbohPhoBiA"
# casefold is a more aggressive lower() - which forces letters to lowecase
formatted_string = string.casefold()
# the reversed function does exactly what you'd expect it to do and takes the thing you want to reverse as an arg
rev_string = reversed(formatted_string)

# the list function takes a string and makes it iterable by creating a list object.  This would output each letter individually (i.e. - ['m', 'a', 'm', 'a'])
# it does what in JS needs two methods (.split() and .join())
if list(formatted_string) == list(rev_string):
    print("Yes, this is a palindrome.")
else:
    print("No, this is not a palindrome.")
