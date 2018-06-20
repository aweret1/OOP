w = input('Наш or Не наш:')
if w == 'Не наш':
    weight = float(input('Вага:'))
    height = float(input('Ріст:'))
    print('IMT:',703*weight/height**2)
elif w == 'Наш':
    weight = float(input('Вага:'))
    height = float(input('Ріст:'))
    print('IMT:',weight/height**2)



import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
