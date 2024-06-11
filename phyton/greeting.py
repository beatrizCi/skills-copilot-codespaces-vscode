#import datetime module

import datetime
# get current time

current_time = datetime.datetime.now()
print(current_time)
# Get current hour
current_hour = current_time.hour
print(current_hour)
# Check if it is morning (before 12 PM)
if current_hour < 12:
    print("Good morning!")
# Check if it is evening (after 16 PM)
elif current_hour >= 16:
    print("Good evening!")