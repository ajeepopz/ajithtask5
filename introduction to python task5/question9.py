#number of words in it

def count_words(input_string):
    words = input_string.split()

    return len(words)

input_str = 'this is ajith kumar'
result = count_words(input_str)

print(f'The numbers of words in the string is: {result}')