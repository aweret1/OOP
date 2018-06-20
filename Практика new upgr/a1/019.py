a = float(input("Вік собаки "))
if a >= 0 : 
    print("Вік людини: {0:.2f}".format(a*5.25)) 
elif a <= 2:
    print ("Вік людини:{0:.2f} ".format(a*5.25))
elif a > 2:
    print("Вік людини {0:.2f}".format((10.5)+((a-2)*4)))
else:
    print("Не може такого бути")




import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
