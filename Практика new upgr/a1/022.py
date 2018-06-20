a = []
while True:
    s = int(input('Цілі числа '))
    a.append(s)
    if s == 0:
        a.sort()
        a.remove(0)
        print(a)
    
        
        
    
import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
