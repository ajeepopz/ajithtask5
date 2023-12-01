#function takes string and returns true r false
 
def is_palindrome(s):
    s = s.replace(" ", "").lower() 
    return s == s[::-1]

input_string = ("appa")
result = is_palindrome(input_string)

if result:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

    