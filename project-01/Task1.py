"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

phone_numbers = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

for sending, receiving, _ in texts:
    phone_numbers.add(sending)
    phone_numbers.add(receiving)

for sending, receiving, _, _ in calls:
    phone_numbers.add(sending)
    phone_numbers.add(receiving)

print(len(phone_numbers))

"""
TASK 1:
How many different telephone numbers are there in the records
Print a message:
"There are <count> different telephone numbers in the records."
"""
