# email_extraction from the sentence
import re
def email_extraction(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

print(email_extraction("Please contact us at    support@example.com or sales@example.com for assistance."))

