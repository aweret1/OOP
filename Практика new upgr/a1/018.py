n = input('Число ')
summa = 0
for i in n:
	summa += int(i)
print("Сума:", summa)



import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")

