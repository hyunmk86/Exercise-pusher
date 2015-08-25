import datetime
import os

# Prototype of app I am designing for android in Python. Calculate your target growth % daily, weekly, monthly or
# however user want to grow(only daily in shown in the script)
# Primary designed for push ups but new feature and new way to use such as adding option for improving specific
# exercise or skill will be added.
def writedate():
    if os.stat("startdate.txt").st_size == 0:
        lineone =2015
        linetwo =8
        linethree =8
        with open("startdate.txt","w+") as fo:
            fo.write("%i \n %i \n %i \n" % (lineone, linetwo, linethree))
    else:
        print "Error, date already exist"

def readdate():
    date = []
    with open("startdate.txt",'r') as fo:
        for line in fo:
            date.append(line.strip())
        return date

def growth():
    today = datetime.date.today()
    other = datetime.date(int(readdate()[0]),int(readdate()[1]),int(readdate()[2]))
    days = today - other
    remain = days.days+(days.days * .1)
    return round(remain)


writedate()
readdate()
print growth()