"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

duration_by_phonenumber = defaultdict(int)

for sending, receiving, _, duration in calls:
    duration_by_phonenumber[sending] += int(duration)
    duration_by_phonenumber[receiving] += int(duration)

max_call_phone_number = ''
max_call_duration = 0
for phone_number, duration in duration_by_phonenumber.items():
    if max_call_duration < duration:
        max_call_duration = duration
        max_call_phone_number = phone_number

args = tuple([max_call_phone_number, max_call_duration])
template = "%s spent the longest time, %s seconds, on the phone during September 2016."
print(template % args)
