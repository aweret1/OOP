temp = (0 , 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100)
far = (32 , 50 , 68 , 86 , 104 , 122 , 140 , 158 , 176 , 194 , 212)
for i in range(len(temp)):
    print("{0} °C{1:>30} F".format(temp[i],far[i]))
        



import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")









