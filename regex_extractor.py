import re 
import json

# opens the file input.txt reads all the text from the file into string raw_text
# encoding="utf-8 to  handle special characters and the with closes thw file after reading

with open("input.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

# Regex for extracting Email patterns 
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Regex for extracting URL patterns 
url_pattern = r"https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?"

# Regex for extracting Phone number patterns
phone_pattern = r"(?:\(\d{3}\)\s?\d{3}[-.\s]\d{4}|\d{3}[-.\s]\d{3}[-.\s]\d{4})"

# Regex for extracting  Time patterns (12-hour and 24-hour formats)
time_pattern = r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?(?:AM|PM))?\b"

# search for string match using re and findall returns a list containing all  matches 
emails = re.findall(email_pattern, raw_text)
urls = re.findall(url_pattern, raw_text)
phones = re.findall(phone_pattern, raw_text)
times = re.findall(time_pattern, raw_text)

# Mask sensitive data before giving an output


def mask_email(email):
    """Hide part of the email to reduce sensitive data exposure"""
    name, domain = email.split("@")
    """the split is used to split the email into name and domain."""
    return name[0] + "***@" + domain

masked_emails = [mask_email(email) for email in emails] #applies mask_email to every email in emails


#dictionary to be as json

output = {
    "emails": masked_emails,
    "urls": urls,
    "phone_numbers": phones,
    "times": times
}

# opens the file and writes the output dictonary to the file in json with 4 spaces of indentation to make it readable.

with open("output.json", "w", encoding="utf-8") as file:
    json.dump(output, file, indent=4)

#prints a message after completion to checkout the .json 

print("Data extraction complete. Check output.json")
