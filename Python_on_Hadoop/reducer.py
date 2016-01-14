#!/usr/bin/env python
#Reducer.py
from intertools import groupby
from operator import itemgetter #itertools prevents too much data from being loaded into memory

SEP = '/t' #note this is a tab seperated file indicates keys and values

class Reducer(object): #API like interaction via a class
	def __init__(self, stream, sep = SEP) #tab is usual and pretty friendly
		self.stream = stream
		self.sep = sep
		
	def emit(self, key, value): #takes a key and value and write to stdout via the sep character
		sys.stdout.write('%s%s%s\n' % (key, self.sep, value))
		
	def reduce(self):
		for current, group in groupby(self, itemgetter(0)): #scans ahead and provides current key and group 
			total = 0 #total itemgetter
			count = 0 #count ot total items
			
			for item in group: #group by self 
				total += item[1]
				count += 1
				
			self.emit(current, float(total)/float(count)) #calculate the average
			
	def __iter__(self):
		for line in self.stream: #seperate by each line
			try: 
				parts = line.split(self.sep) #yeilds the key
				yield parts[0], float(parts[1]) #yields the value, cast into a float
			except:
				continue
			
if __name__ == '__main__':
	reducer = Reducer(sys.stdin)
	reduce.reduce()
