# Problem return the average word length given a sentence
# Edge case warning - punctuation

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"


def solution(sentence):  # takes in sentence as a parameter
    for p in "!?',;.":  # this line addresses the punctuation and p goes through the input and finds the punctuation
        # sentence is saved as the original sentence, but where there are punctuation, it adds a blank space instead
        sentence = sentence.replace(p, ' ')
    # create words var which is the sentence split up (separated by space)
    words = sentence.split()
    # rounds the average to two decimal places - dividing the length of each word  in the now split sentence (words) by the whole/total of words (aka the amount of words in the sentence)
    return round(sum(len(word) for word in words) / len(words), 2)


print(solution(sentence1))
print(solution(sentence2))

# replace() returns a new string, replacing the old string with whatever is passed in
# split() splits a string into a list - default separation is by whitespace, but you can also specify
