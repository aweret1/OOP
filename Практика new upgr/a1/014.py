s = input('Write a letter:')
if s in 'aeiou':
    print('Голосна')
elif s in 'bcdqwrtpsfghjklzxvnm':
    print('Приголосна')
else:
    print('Можливо голосна або приголосна')


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
