import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# Updated regex to exclude emails from 'exclude.com'
pattern = r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com\b)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# Find all emails except those from 'exclude.com'
emails = re.findall(pattern, text)

print(emails)
