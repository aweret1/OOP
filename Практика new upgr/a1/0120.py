br = int(input("Вчорашній хліб (буханки)"))

print("Вартість такого хліба {0:>30} грн\nСкидка на такий хліб{1:>30} грн\nОтже це коштуватиме {2:>30} грн"
      .format(br*8.50, (br*8.50)*0.6, (br*8.50)-((br*8.50)*0.6)))


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
