p = float(input('Тиск у кП'))
print('Атмосфери {0:.2f}\nФт/дм {1:.2f}\nмм рт стопчика {2:.2f}'.format(p*0.0098 , p*0.145 , p*7.5))

import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
