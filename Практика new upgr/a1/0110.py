a = int(input('Кількість штук:'))
s = int(input('Кількість штукенцій:'))
print('Штук {0:.2f} гр\nШтукенцій {1:.3f}'.format(a*0.075,s*.112))


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
