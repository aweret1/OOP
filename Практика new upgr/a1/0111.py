s = float(input('Ріст в сантиметрах'))
print('Ріст в дюймах {0:.1f} \nРіст в футах {1:.1f}'.format(s/2.54,(s/2.54)/12))


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
