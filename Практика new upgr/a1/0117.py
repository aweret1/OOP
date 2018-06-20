money = float(input("Скільки грошей поклали на картку?"))

print("Через рік {0:.2f}\nЧерез два роки {1:.2f}\nЧерез три роки {2:.2f}"
      .format(money*1.14, (money*1.14)*1.14, (((money*1.14)*1.14)*1.14)))


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
