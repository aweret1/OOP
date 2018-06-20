a = int(input('перше число:'))
b = int(input('друге число:'))
c = int(input('третє число:'))
print('Найменше',min(a, b, c))
print('Середнє',(a+b+c)-min(a, b, c)-max(a, b, c))
print('Найбільше',max(a, b, c))



import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
