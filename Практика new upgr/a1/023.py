import random as r
import itertools as itert


s = [1,2,3]
r.shuffle(s)
print(s)
print (list(itert.permutations(s)))


import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
