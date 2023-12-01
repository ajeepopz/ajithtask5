##vowels

def count_vowels(string):
    string = string.lower()
    total_vowels = 0
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for char in string:
        if char in 'aeiou':
            total_vowels += 1
            vowel_counts[char] += 1
    
    return total_vowels, vowel_counts

# Given string
given_string = "Guvi Geeks Network Privated Limited"

# Calculate total vowels and individual counts
total_vowels, individual_counts = count_vowels(given_string)

print("Total vowels:", total_vowels)
print("Count of each individual vowel:")
for vowel, count in individual_counts.items():
    print(f"{vowel}: {count}")