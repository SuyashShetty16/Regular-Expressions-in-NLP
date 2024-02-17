import re

def extract_patterns(text):
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    phone_numbers = re.findall(r'\+?\d{2}[-.\s]?\d{10}\b', text)
    hashtags = re.findall(r'\#\w+', text)
    repetitive_chars = re.findall(r'(\w)\1{2,}', text)

    # Clean the text
    clean_text = text
    clean_text = re.sub(r'\bhe+y\b', 'hey', clean_text)
    clean_text = re.sub(r'\bver+r+y\b', 'very', clean_text)
    clean_text = re.sub(r'\blo+ng\b', 'long', clean_text)
    clean_text = re.sub(r'(\w)\1{2,}', r'\1', clean_text)

    return urls, emails, phone_numbers, hashtags, repetitive_chars, clean_text.strip()

# Sample text with an actual phone number
sample_text = """
Here is a sample text containing various patterns such as URLs like https://example.com, 
emails like test@example.com, phone numbers like +91 7028583899, 
hashtags like #NLP #Python, and repetitive characters like heyyy this is a verrrry loong texttt
"""

# Extract patterns from the sample text
urls, emails, phone_numbers, hashtags, repetitive_chars, clean_text = extract_patterns(sample_text)

# Print the original text
print("Original Text:")
print(sample_text)

# Print the extracted patterns
print("\nExtracted Patterns:")
print("URLs:", urls)
print("Emails:", emails)
print("Phone Numbers:", phone_numbers)
print("Hashtags:", hashtags)
print("Repetitive Characters:", repetitive_chars)

# Print the cleaned text
print("\nCleaned Text:")
print(clean_text)
