
#remove the vowels from string

def remove_vowels(input_string):
    vowels = "aeiou"
    return "".join(char for char in input_string if char not in vowels)

input_str = "hi this ajith kumar from guvi"
result = remove_vowels(input_str)
print("String with vowels removed:", result)