# Update file dates below if they fall between a certain range.
# Use thusly:
# assignFileDateModified C:\Temp

from sys import argv
import datetime
import os

path = argv[1]
fromTime = datetime.datetime(2000, 1, 1).timestamp() # exclusive
untilTime = datetime.datetime(2000, 1, 2).timestamp() # exclusive

def update(path):
	print(f'Updating file {path}')
	os.utime(path)

def setTimes(path):
	print(path)
	entries = [path+'\\'+name for name in os.listdir(path)]
	dirs = [e for e in entries if os.path.isdir(e)]
	changeFiles = [
		e for e in entries
		if os.path.isfile(e)
		and fromTime < os.path.getmtime(e) < untilTime
	]
	[setTimes(entry) for entry in dirs]
	[update(entry) for entry in changeFiles]

setTimes(path)
