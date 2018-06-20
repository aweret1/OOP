w = float(input('Ширина поля :'))
l = float(input('Довжина поля :'))
print('Площа поля {0:.1f}\nПлоща в гектарах {1:.1f}\nПлоща в акрах {2:.1f}'
      .format(w*l, (w*l)*0.0001, (w*l)*0.00024))


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
