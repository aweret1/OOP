temp = float(input('Температура в градусах по Цельсію:'))
print('Конвертуєм в Фаренгейт:{0:.2f}'.format((temp*1.8)+32))
print('Конвертуєм в Кельвіна:{0:.2f}'.format(temp+273.15))


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
