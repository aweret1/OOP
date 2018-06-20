m = float(input('Хвилини: '))
mes = float(input('Меседжи: '))
tarif = 15
if 0 <= m <= 200:
    tarif += 0
elif m > 200:
    money = (m - 200) * 0.17
    tarif += money
else:
    print('')

if 0 <= mes <= 50:
    tarif += 0
elif mes > 50:
    money = (mes - 50) * 0.15
    tarif += money
else:
    print('')


c = tarif + 0.44 + (tarif * 0.05)

print('Базова плата за користування: {0:>.2f}'.format(tarif))
print('Загалний рахунок для користувача: {0:>.2f}'.format(c))


import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Іщенко')
