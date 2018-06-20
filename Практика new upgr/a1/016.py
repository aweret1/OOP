first = float(input('Вартість першої страви:'))
second = float(input('Вартість другої страви:'))
print('Вартість всих страв',first+second,'\Чайові:',(first+second)*0.14,'грн','Податок:',(first+second)*0.18,'грн')


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
