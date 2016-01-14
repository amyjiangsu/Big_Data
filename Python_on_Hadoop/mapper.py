#!/usr/bin/env python
#Mapper.py
import csv #data on disc is a csv file	
import sys #system commands

SEP = '/t' #note this is a tab seperated file indicates keys and values

class Mapper(object): #API like interaction via a class
	def __init__(self, stream, sep = SEP) #tab is usual and pretty friendly
		self.stream = stream
		self.sep = sep
		
	def emit(self, key, value): #takes a key and value and write to stdout via the sep character
		sys.stdout.write('%s%s%s\n' % (key, self.sep, value))
		
	def map(self):
		reader = csv.reader(self.stream) #creates a csv reader from the string
		for row in reader: 
			self.emit(row[8], row[31]) #emit 9th position from row as KEY, and 32nd as VALUE
			
if __name__ == '__main__':
	mapper = Mapper(sys.stdin) #initiatized via standardin
	mapper.map()
