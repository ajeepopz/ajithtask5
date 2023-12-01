#function in unique characters

def count_unique_characters(input_string):
    unique_chars = set(input_string)
    
    return len(unique_chars)

example_string = "ajith,kumar !"
unique_count = count_unique_characters(example_string)
print("Number of unique characters:", unique_count)