#longest common substrings

def longest_common_substring(str1, str2):
    
    long1 = len(str1)
    long2 = len(str2)
    longest_length = 0
    end_index = 0
    
    table = [[0] * (long2 + 1) for _ in range(long1 + 1)]
    
    for i in range(long1 + 1):
        for j in range(long2 + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > longest_length:
                    longest_length = table[i][j]
                    end_index = i - 1
            else:
                table[i][j] = 0
    
    
    longest_substring = str1[end_index - longest_length + 1: end_index + 1]
    return longest_substring

string1 = "12345"
string2 = "123456789"
result = longest_common_substring(string1, string2)

print(f"The longest common substring is: '{result}'")

