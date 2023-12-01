#most frequent character

def most_frequent_character(input_string):
   
    char_unique = {}

    for char in input_string:
        if char.isalpha():  
            char = char.lower()  
            char_unique[char] = char_unique.get(char, 0) + 1

    most_frequent_char = max(char_unique, key=char_unique.get)

    return most_frequent_char

input_str = "Ajee_popZ!"
result = most_frequent_character(input_str)

print(f"The most frequent character is: '{result}'")