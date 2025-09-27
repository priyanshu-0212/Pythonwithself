import time #importing time from python libraries

ts = (time.strftime("%Y"+" " + "%m" +" %d")) #printing year, month and date
print(ts)
ts = int(time.strftime("%H")) #printing the hour at which we are now
print(ts)
ts = int(time.strftime("%M")) #printing the minute at which we are now
print(ts)
ts = int(time.strftime("%S")) #printing the second at which we are now
print(ts)
