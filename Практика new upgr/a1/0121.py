n = int(input("Введіть ціле число "))

print('Addition of all numbers {0:.2f}'.format((n*(n+1))/2))


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
