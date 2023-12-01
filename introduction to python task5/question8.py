#anagram

def are_anagram(str1, str2):
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    return sorted(str1) == sorted(str2)

string1 = "heart"
string2 = "earth"
result = are_anagram(string1, string2)

if result:
    print(f'"{string1}" and "{string2}" are anagram')
else:
    print(f'"{string1}" and "{string2}" are not anagram')

    