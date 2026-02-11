# question 7:Word count in a sentence

def word_count(sentence):
    words = sentence.strip().split()
    return len(words)

count =  word_count("  This is   Python  ")
print(f"The number of words in the sentence is: {count}")

# question 8:Vowel counter

def vowel_counter(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
print(vowel_counter("Hello World!"))