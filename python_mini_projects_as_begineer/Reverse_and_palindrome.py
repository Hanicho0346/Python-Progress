# question 8: reverse worrds in sentence

def reverse_words(sentence):
    words=sentence.split()
    reversed_words=words[::-1]
    return ' '.join(reversed_words)

print(reverse_words("Hello World!"))


# question 9:palindrome checker

def palindrome_checker(text):
    text = text.lower().replace(" ","")
    return text == text[::-1]
print(palindrome_checker("A man a plan a canal Panama"))