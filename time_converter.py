#Convert number of seconds

total_seconds = float(input('Enter the number of seconds: '))

hours = total_seconds // 3600

minutes = (total_seconds // 60) % 60

seconds = total_seconds % 60

print('The number of time in hours, minutes and seconds are: ')
print('Hours: ', hours)
print('Minutes: ', minutes)
print('Seconds: ', seconds)