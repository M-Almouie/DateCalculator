# Author: Daniel Al Mouiee
# Date: 28/08/2018
# Python script to calculate the number of days between two given dates
# Assumptions:
#	1: Dates are between 01/01/1900 and 12/12/2999
#	2: The start and end DAY are NOT counted 

#!/usr/bin/python3
import sys, math, fileinput
res = 'invalid'
shortMonth = [4,6,9,11]
longMonth = [1,3,5,7,8,10,12]

def checkInputErrors(x, y):
	error = 0
	if x[0] < 0 or x[0] > 31 or y[0] < 0 or y[0] > 31:
		error = 1
	elif x[1] < 0 or x[1] > 12 or y[1] < 0 or y[1] > 12:
		error = 1
	elif x[2] < 1900 or x[2] > 2999 or y[2] < 1900 or y[2] > 2999:
		error = 1
	if error == 1:
		print("Error: Please make sure that the dates follow the following rules\n\
1: Dates are between 01/01/1900 and 12/12/2999\n\
2: Days are between 0 and 31 (inclusive)\n\
3: Months are between 0 and 12(inclusive)\n")
		exit(1)
	return
	
def swapDates(x,y):
	bool = 0
	if x[2] < y[2]:
		bool = 1
	elif x[1] < y[1]:
		bool = 1
	return bool

def endDayMonth(x):
	if x[1] in shortMonth:
		temp = 30 - x[0]
	elif x[1] in longMonth:
		temp = 31 - x[0]
	else:
		if checkLeapYear(x[2]) == 0:
			temp = 28 - x[0]
		else:
			temp = 29 - x[0]
	return temp

def startDaysSoFar(x):
	if x[1] == 1:
		daysSoFar = x[0]
	else:
		temp = 0
		for i in range(1,x[1]):
			if checkLeapYear(x) == 1 and i == 2:
				temp += checkLeapMonth(i)
			else:
				temp += checkMonth(i)
		daysSoFar = x[0] + temp
	if checkLeapYear(x) == 0:
		daysSoFar = 365 - daysSoFar
	else:
		daysSoFar = 366 - daysSoFar
	return daysSoFar

def endDaysSoFar(x):
	if x[1] == 1:
		daysSoFar = x[0]
	else:
		temp = 0
		for i in range(1,x[1]):
			if checkLeapYear(x) == 1 and i == 2:
				temp += checkLeapMonth(i)
			else:
				temp += checkMonth(i)
		daysSoFar = x[0] + temp
	return daysSoFar

def checkMonth(x):
	if x in shortMonth:
		temp = 30
	elif x in longMonth:
		temp = 31
	else:
		temp = 28
	return temp
	
def checkLeapMonth(x):
	if x in shortMonth:
		temp = 30
	elif x in longMonth:
		temp = 31
	else:
		temp = 29
	return temp

def checkLeapYear(x):
	bool = 0
	if ((x[2] % 4) == 0):
		if x[2] % 100 == 0:
			if x[2] % 400 == 0:
				bool = 1
			else:
				bool = 0
		else:
			bool = 1
	else:
		bool = 0

def checkLeapYearNum(x):
	bool = 0
	if ((x % 4) == 0):
		if x % 100 == 0:
			if x % 400 == 0:
				bool = 1
			else:
				bool = 0
		else:
			bool = 1
	else:
		bool = 0

def checkYearDay(x):
	if checkLeapYearNum(x) == 1:
		return 366
	else:
		return 365

###########################################################
# Main Program
if sys.argv[1] == '-h':
	print("Python script to calculate the number of days between two given dates\n\
Input 2 dates between 01/01/1900 and 12/12/2999 in the following form: DD/MM/YYYY\n\
Or supply a text .txt file containing dates")
	exit()
startDate = list(map(int, sys.argv[1].split('/')))
endDate = list(map(int, sys.argv[2].split('/')))
# Error checking 
checkInputErrors(startDate, endDate)
# Swap Dates if end < start
if swapDates(endDate,startDate) == 1:
	temp = startDate
	startDate = endDate
	endDate = temp
	
#Same Year
if endDate[2] == startDate[2]:
	#Same Month
	if endDate[1] == startDate[1]:
		#Same Day
		if endDate[0] == startDate[0]:
			res = 0
		else:
			#years = abs(endDate[2]-startDate[2])
			#months = abs(endDate[1]-startDate[1])
			days = abs(endDate[0] - startDate[0]) - 1
			res = days
	else:
		#Successive months
		if abs(endDate[1]-startDate[1]) == 1:
			temp1 = endDayMonth(startDate)
			temp2 = endDate[0]
			res = temp1 + temp2 - 1
		#Not successive months
		else:
			temp1 = endDayMonth(startDate)
			temp2 = endDate[0]
			temp3 = 0
			for i in range(startDate[1]+1,endDate[1]):
				temp3 += checkMonth(i)
			res = temp1 + temp2 + temp3 - 1
#Different Year
else:
	#Successive years
	if abs(endDate[2]-startDate[2]) == 1:
		temp1 = startDaysSoFar(startDate)
		temp2 = endDaysSoFar(endDate)
		res = temp1 + temp2 - 1
	#Not sucessive years
	else:
		temp1 = startDaysSoFar(startDate)
		temp2 = endDaysSoFar(endDate)
		temp3 = 0
		for i in range(startDate[2]+1,endDate[2]):
			temp3 += checkYearDay(i)		
		res = temp1 + temp2 + temp3
print("Days between dates = "+str(res))