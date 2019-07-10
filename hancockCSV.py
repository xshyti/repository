import csv
import datetime
import times
from outputCSV import toCSV, createCSV

def header():
    createCSV()

def condos():
    opened = open('HX_CONDOS_Chart.csv')
    reader = csv.reader(opened)
    condos = list(reader)
    finish = len(condos) - 1
    toCSV(["Report Start", "Report Finish"])
    toCSV([condos[1][0], condos[finish][0]])
    toCSV(["Meter Name", "KBTU Usage"])
    BTUs = []
    averages = []
    i = 1
    while i < len(condos):
        BTUs.append(((float(condos[i][2]) - float(condos[i][1])) * 499 * float(condos[i][3])) / 1000)
        i = i + 1
    chunks = [BTUs[x:x+4] for x in range(0, len(BTUs), 4)]
    for group in chunks:
        averages.append(sum(group)/len(group))
    totalSum = sum(averages)
    print("Condos:")
    print(totalSum)
    row = ["Condos", totalSum]
    toCSV(row)

def he2_247():
    opened = open('HX_2_Chart.csv')
    reader = csv.reader(opened)
    he2 = list(reader)
    BTUs = []
    averages = []
    i = 1
    while i < len(he2):
        BTUs.append(((float(he2[i][2]) - float(he2[i][1])) * 499 * float(he2[i][3])) / 1000)
        i = i + 1
    chunks = [BTUs[x:x+4] for x in range(0, len(BTUs), 4)]
    for group in chunks:
        averages.append(sum(group)/len(group))
    totalSum = sum(averages)
    print('HE2_247:')
    print(totalSum)
    row = ["HE2 - 24/7", totalSum]
    toCSV(row)

def he2():
    opened = open('HX_2_Chart.csv')
    reader = csv.reader(opened)
    he2 = list(reader)
    BTUs = []
    averages = []
    i = 1
    while i < len(he2):
        if times.convertDateTime(he2[i][0]).date().weekday() == 6:
            if times.easyTime[he2[i][0][-15:]] >= 0 and times.easyTime[he2[i][0][-15:]] < 1000:
                BTUs.append(((float(he2[i][2]) - float(he2[i][1])) * 499 * float(he2[i][3])) / 1000)
            elif times.easyTime[he2[i][0][-15:]] >= 2300:
                BTUs.append(((float(he2[i][2]) - float(he2[i][1])) * 499 * float(he2[i][3])) / 1000)
		
        elif times.convertDateTime(he2[i][0]).date().weekday() == 0:
            if times.easyTime[he2[i][0][-15:]] >= 0 and times.easyTime[he2[i][0][-15:]] < 800:
                BTUs.append(((float(he2[i][2]) - float(he2[i][1])) * 499 * float(he2[i][3])) / 1000)
            elif times.easyTime[he2[i][0][-15:]] >= 2330:
                BTUs.append(((float(he2[i][2]) - float(he2[i][1])) * 499 * float(he2[i][3])) / 1000)
				
        elif times.convertDateTime(he2[i][0]).date().weekday() == 1:
            if times.easyTime[he2[i][0][-15:]] >= 0 and times.easyTime[he2[i][0][-15:]] < 800:
                BTUs.append(((float(he2[i][2]) - float(he2[i][1])) * 499 * float(he2[i][3])) / 1000)
            elif times.easyTime[he2[i][0][-15:]] >= 2330:
                BTUs.append(((float(he2[i][2]) - float(he2[i][1])) * 499 * float(he2[i][3])) / 1000)
				
        elif times.convertDateTime(he2[i][0]).date().weekday() == 2:
            if times.easyTime[he2[i][0][-15:]] >= 0 and times.easyTime[he2[i][0][-15:]] < 800:
                BTUs.append(((float(he2[i][2]) - float(he2[i][1])) * 499 * float(he2[i][3])) / 1000)
            elif times.easyTime[he2[i][0][-15:]] >= 2330:
                BTUs.append(((float(he2[i][2]) - float(he2[i][1])) * 499 * float(he2[i][3])) / 1000)
				
        elif times.convertDateTime(he2[i][0]).date().weekday() == 3:
            if times.easyTime[he2[i][0][-15:]] >= 0 and times.easyTime[he2[i][0][-15:]] < 800:
                BTUs.append(((float(he2[i][2]) - float(he2[i][1])) * 499 * float(he2[i][3])) / 1000)
				
        elif times.convertDateTime(he2[i][0]).date().weekday() == 4:
            if times.easyTime[he2[i][0][-15:]] >= 100 and times.easyTime[he2[i][0][-15:]] < 830:
                BTUs.append(((float(he2[i][2]) - float(he2[i][1])) * 499 * float(he2[i][3])) / 1000)
				
        elif times.convertDateTime(he2[i][0]).date().weekday() == 5:
            if times.easyTime[he2[i][0][-15:]] >= 2300 and times.easyTime[he2[i][0][-15:]] <= 2345:
                BTUs.append(((float(he2[i][2]) - float(he2[i][1])) * 499 * float(he2[i][3])) / 1000)
        i = i + 1
    chunks = [BTUs[x:x+4] for x in range(0, len(BTUs), 4)]
    for group in chunks:
        averages.append(sum(group)/len(group))
    totalSum = sum(averages)
    print("HE2:")
    print(totalSum)
    row = ["HE2", totalSum]
    toCSV(row)

def he3():
    opened = open('HX_3_Chart.csv')
    reader = csv.reader(opened)
    he3 = list(reader)
    BTUs = []
    averages = []
    i = 1
    while i < len(he3):
        if times.convertDateTime(he3[i][0]).date().weekday() == 6:
            if times.easyTime[he3[i][0][-15:]] >= 0 and times.easyTime[he3[i][0][-15:]] < 1000:
                BTUs.append(((float(he3[i][2]) - float(he3[i][1])) * 499 * float(he3[i][3])) / 1000)
            elif times.easyTime[he3[i][0][-15:]] >= 2300:
                BTUs.append(((float(he3[i][2]) - float(he3[i][1])) * 499 * float(he3[i][3])) / 1000)
		
        elif times.convertDateTime(he3[i][0]).date().weekday() == 0:
            if times.easyTime[he3[i][0][-15:]] >= 0 and times.easyTime[he3[i][0][-15:]] < 800:
                BTUs.append(((float(he3[i][2]) - float(he3[i][1])) * 499 * float(he3[i][3])) / 1000)
            elif times.easyTime[he3[i][0][-15:]] >= 2330:
                BTUs.append(((float(he3[i][2]) - float(he3[i][1])) * 499 * float(he3[i][3])) / 1000)
				
        elif times.convertDateTime(he3[i][0]).date().weekday() == 1:
            if times.easyTime[he3[i][0][-15:]] >= 0 and times.easyTime[he3[i][0][-15:]] < 800:
                BTUs.append(((float(he3[i][2]) - float(he3[i][1])) * 499 * float(he3[i][3])) / 1000)
            elif times.easyTime[he3[i][0][-15:]] >= 2330:
                BTUs.append(((float(he3[i][2]) - float(he3[i][1])) * 499 * float(he3[i][3])) / 1000)
				
        elif times.convertDateTime(he3[i][0]).date().weekday() == 2:
            if times.easyTime[he3[i][0][-15:]] >= 0 and times.easyTime[he3[i][0][-15:]] < 800:
                BTUs.append(((float(he3[i][2]) - float(he3[i][1])) * 499 * float(he3[i][3])) / 1000)
            elif times.easyTime[he3[i][0][-15:]] >= 2330:
                BTUs.append(((float(he3[i][2]) - float(he3[i][1])) * 499 * float(he3[i][3])) / 1000)
				
        elif times.convertDateTime(he3[i][0]).date().weekday() == 3:
            if times.easyTime[he3[i][0][-15:]] >= 0 and times.easyTime[he3[i][0][-15:]] < 800:
                BTUs.append(((float(he3[i][2]) - float(he3[i][1])) * 499 * float(he3[i][3])) / 1000)
				
        elif times.convertDateTime(he3[i][0]).date().weekday() == 4:
            if times.easyTime[he3[i][0][-15:]] >= 100 and times.easyTime[he3[i][0][-15:]] < 830:
                BTUs.append(((float(he3[i][2]) - float(he3[i][1])) * 499 * float(he3[i][3])) / 1000)
				
        elif times.convertDateTime(he3[i][0]).date().weekday() == 5:
            if times.easyTime[he3[i][0][-15:]] >= 2300 and times.easyTime[he3[i][0][-15:]] <= 2345:
                BTUs.append(((float(he3[i][2]) - float(he3[i][1])) * 499 * float(he3[i][3])) / 1000)
        i = i + 1
    chunks = [BTUs[x:x+4] for x in range(0, len(BTUs), 4)]
    for group in chunks:
        averages.append(sum(group)/len(group))
    totalSum = sum(averages)
    print("HE3:")
    print(totalSum)
    row = ["HE3", totalSum]
    toCSV(row)


def s17():
    opened = open('HX_S17_Chart.csv')
    reader = csv.reader(opened)
    s17 = list(reader)
    BTUs = []
    averages = []
    i = 1
    while i < len(s17):
        BTUs.append(((float(s17[i][2]) - float(s17[i][1])) * 499 * float(s17[i][3])) / 1000)
        i = i + 1
    chunks = [BTUs[x:x+4] for x in range(0, len(BTUs), 4)]
    for group in chunks:
        averages.append(sum(group)/len(group))
    totalSum = sum(averages)
    print("S17:")
    print(totalSum)
    row = ["S17", totalSum]
    toCSV(row)

def s19():
    opened = open('HX_S19_Chart.csv')
    reader = csv.reader(opened)
    s19 = list(reader)
    BTUs = []
    averages = []
    i = 1
    while i < len(s19):
        if times.convertDateTime(s19[i][0]).date().weekday() == 6:
            if times.easyTime[s19[i][0][-15:]] >= 0 and times.easyTime[s19[i][0][-15:]] < 900:
                BTUs.append(((float(s19[i][2]) - float(s19[i][1])) * 499 * float(s19[i][3])) / 1000)
            elif times.easyTime[s19[i][0][-15:]] >= 2300:
                BTUs.append(((float(s19[i][2]) - float(s19[i][1])) * 499 * float(s19[i][3])) / 1000)
        
        elif times.convertDateTime(s19[i][0]).date().weekday() == 0:
            if times.easyTime[s19[i][0][-15:]] >= 0 and times.easyTime[s19[i][0][-15:]] < 900:
                BTUs.append(((float(s19[i][2]) - float(s19[i][1])) * 499 * float(s19[i][3])) / 1000)
            elif times.easyTime[s19[i][0][-15:]] >= 2300:
                BTUs.append(((float(s19[i][2]) - float(s19[i][1])) * 499 * float(s19[i][3])) / 1000)
        
        elif times.convertDateTime(s19[i][0]).date().weekday() == 1:
			if times.easyTime[s19[i][0][-15:]] >= 0 and times.easyTime[s19[i][0][-15:]] < 900:
				BTUs.append(((float(s19[i][2]) - float(s19[i][1])) * 499 * float(s19[i][3])) / 1000)
			elif times.easyTime[s19[i][0][-15:]] >= 2300:
				BTUs.append(((float(s19[i][2]) - float(s19[i][1])) * 499 * float(s19[i][3])) / 1000)
        
        elif times.convertDateTime(s19[i][0]).date().weekday() == 2:
			if times.easyTime[s19[i][0][-15:]] >= 0 and times.easyTime[s19[i][0][-15:]] < 900:
				BTUs.append(((float(s19[i][2]) - float(s19[i][1])) * 499 * float(s19[i][3])) / 1000)
			elif times.easyTime[s19[i][0][-15:]] >= 2300:
				BTUs.append(((float(s19[i][2]) - float(s19[i][1])) * 499 * float(s19[i][3])) / 1000)
        
        elif times.convertDateTime(s19[i][0]).date().weekday() == 3:
			if times.easyTime[s19[i][0][-15:]] >= 0 and times.easyTime[s19[i][0][-15:]] < 900:
				BTUs.append(((float(s19[i][2]) - float(s19[i][1])) * 499 * float(s19[i][3])) / 1000)
			elif times.easyTime[s19[i][0][-15:]] >= 2300:
				BTUs.append(((float(s19[i][2]) - float(s19[i][1])) * 499 * float(s19[i][3])) / 1000)
        
        elif times.convertDateTime(s19[i][0]).date().weekday() == 4:
			if times.easyTime[s19[i][0][-15:]] >= 0 and times.easyTime[s19[i][0][-15:]] < 900:
				BTUs.append(((float(s19[i][2]) - float(s19[i][1])) * 499 * float(s19[i][3])) / 1000)
			elif times.easyTime[s19[i][0][-15:]] >= 2300:
				BTUs.append(((float(s19[i][2]) - float(s19[i][1])) * 499 * float(s19[i][3])) / 1000)
        
        elif times.convertDateTime(s19[i][0]).date().weekday() == 5:
			if times.easyTime[s19[i][0][-15:]] >= 0 and times.easyTime[s19[i][0][-15:]] < 900:
				BTUs.append(((float(s19[i][2]) - float(s19[i][1])) * 499 * float(s19[i][3])) / 1000)
			elif times.easyTime[s19[i][0][-15:]] >= 2300:
				BTUs.append(((float(s19[i][2]) - float(s19[i][1])) * 499 * float(s19[i][3])) / 1000)
        i = i + 1
    chunks = [BTUs[x:x+4] for x in range(0, len(BTUs), 4)]
    for group in chunks:
        averages.append(sum(group)/len(group))
    totalSum = sum(averages)
    print("S19:")
    print(totalSum)
    row = ["S19", totalSum]
    toCSV(row)

def s45():
    opened = open('HX_S45_Chart.csv')
    reader = csv.reader(opened)
    s45 = list(reader)
    BTUs = []
    averages = []
    i = 1
    while i < len(s45):
        if times.convertDateTime(s45[i][0]).date().weekday() == 6:
            if times.easyTime[s45[i][0][-15:]] >= 0 and times.easyTime[s45[i][0][-15:]] < 1200:
                BTUs.append(((float(s45[i][2]) - float(s45[i][1])) * 499 * float(s45[i][3])) / 1000)
            elif times.easyTime[s45[i][0][-15:]] >= 2300:
                BTUs.append(((float(s45[i][2]) - float(s45[i][1])) * 499 * float(s45[i][3])) / 1000)
        
        elif times.convertDateTime(s45[i][0]).date().weekday() == 0:
            if times.easyTime[s45[i][0][-15:]] >= 0 and times.easyTime[s45[i][0][-15:]] < 900:
                BTUs.append(((float(s45[i][2]) - float(s45[i][1])) * 499 * float(s45[i][3])) / 1000)
            elif times.easyTime[s45[i][0][-15:]] >= 2300:
                BTUs.append(((float(s45[i][2]) - float(s45[i][1])) * 499 * float(s45[i][3])) / 1000)
        
        elif times.convertDateTime(s45[i][0]).date().weekday() == 1:
			if times.easyTime[s45[i][0][-15:]] >= 0 and times.easyTime[s45[i][0][-15:]] < 900:
				BTUs.append(((float(s45[i][2]) - float(s45[i][1])) * 499 * float(s45[i][3])) / 1000)
			elif times.easyTime[s45[i][0][-15:]] >= 2300:
				BTUs.append(((float(s45[i][2]) - float(s45[i][1])) * 499 * float(s45[i][3])) / 1000)
        
        elif times.convertDateTime(s45[i][0]).date().weekday() == 2:
			if times.easyTime[s45[i][0][-15:]] >= 0 and times.easyTime[s45[i][0][-15:]] < 900:
				BTUs.append(((float(s45[i][2]) - float(s45[i][1])) * 499 * float(s45[i][3])) / 1000)
			elif times.easyTime[s45[i][0][-15:]] >= 2300:
				BTUs.append(((float(s45[i][2]) - float(s45[i][1])) * 499 * float(s45[i][3])) / 1000)
        
        elif times.convertDateTime(s45[i][0]).date().weekday() == 3:
			if times.easyTime[s45[i][0][-15:]] >= 0 and times.easyTime[s45[i][0][-15:]] < 900:
				BTUs.append(((float(s45[i][2]) - float(s45[i][1])) * 499 * float(s45[i][3])) / 1000)
			elif times.easyTime[s45[i][0][-15:]] >= 2300:
				BTUs.append(((float(s45[i][2]) - float(s45[i][1])) * 499 * float(s45[i][3])) / 1000)
        
        elif times.convertDateTime(s45[i][0]).date().weekday() == 4:
			if times.easyTime[s45[i][0][-15:]] >= 0 and times.easyTime[s45[i][0][-15:]] < 900:
				BTUs.append(((float(s45[i][2]) - float(s45[i][1])) * 499 * float(s45[i][3])) / 1000)
			elif times.easyTime[s45[i][0][-15:]] >= 2300:
				BTUs.append(((float(s45[i][2]) - float(s45[i][1])) * 499 * float(s45[i][3])) / 1000)
        
        elif times.convertDateTime(s45[i][0]).date().weekday() == 5:
			if times.easyTime[s45[i][0][-15:]] >= 0 and times.easyTime[s45[i][0][-15:]] < 900:
				BTUs.append(((float(s45[i][2]) - float(s45[i][1])) * 499 * float(s45[i][3])) / 1000)
			elif times.easyTime[s45[i][0][-15:]] >= 2300:
				BTUs.append(((float(s45[i][2]) - float(s45[i][1])) * 499 * float(s45[i][3])) / 1000)
        i = i + 1
    chunks = [BTUs[x:x+4] for x in range(0, len(BTUs), 4)]
    for group in chunks:
        averages.append(sum(group)/len(group))
    totalSum = sum(averages)
    print("S45:")
    print(totalSum)
    row = ["S45", totalSum]
    toCSV(row)
    toCSV([""])




header()
condos()
he2_247()
he2()
he3()
s17()
s19()
s45()