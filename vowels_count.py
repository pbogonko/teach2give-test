# Write a program that counts the number of vowels in a sentence.

def count_vowels(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0
    for char in sentence:
        char_lower = char.lower()
        if char_lower in vowels:
            vowel_count += 1
    
    return vowel_count

input_sentence = input("Enter a sentence: ")
result = count_vowels(input_sentence)
print("Number of vowels:", result)