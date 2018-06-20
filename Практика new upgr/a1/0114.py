m = input('Назва місяця:')
if m == "Січень" or m == "Березень" or m == "Травень" or m == "Липень" or m == "Серпень" or m == "Жовтень" or m == "Грудень":
    print('31 день')
elif m == "Квітень" or m == "Травень" or m == "Вересень" or m == "Листопад":
    print('30 днів')
elif m == "Лютий":
    j = input ('Високосний рік?')
    if j == "так":
        print('29 днів')
    elif j == "ні":
        print('28 днів')
    else:
        print ('Потрібна назва місяця')



import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")          
