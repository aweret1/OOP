a = [1,2,3,4,1,6,4]
b = a.copy()
print(set(a))
del b[3]
del b[2]
del b[0]
print(b)
            
import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
