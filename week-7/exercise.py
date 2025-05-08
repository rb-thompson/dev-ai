from collections import Counter

# Count word frequencies in a sentence
sentence = "I’ve critically evaluated sources to avoid overhyping claims, focusing on measurable progress and expert skepticism."
word_counts = Counter(sentence.split())
print(word_counts)

# Get the 3 most common words
print(word_counts.most_common(3))


from pathlib import Path
import datetime

# Create a Path object for the current directory
current_dir = Path('.')

# List all files in the current directory
python_files = [file for file in current_dir.glob('*.py')]
print("Python files:", python_files)

# Create a new directory and a file
new_dir = current_dir / 'backup-files'
new_dir.mkdir(exist_ok=True)
new_file = new_dir / 'notes.txt'
new_file.write_text(f"Python wrote this file on {datetime.datetime.now()}")
print(f"Created file: {new_file}, Content: {new_file.read_text()}")


import secrets
import string

# secrets is critical for security tasks like generating API keys, 
# passwords, or tokens, where random would be insecure

# Generate a secure random token
token = secrets.token_hex(16)
print(f"Secure token: {token}")

# Generate a random password
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for _ in range(12))
print(f"Random password: {password}")

import csv

# Read a CSV file
with open('stream-data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Single expression if-else statement
number = 319
is_even = "even" if number % 2 == 0 else "odd"
print(f"The number {number} is {is_even}.")