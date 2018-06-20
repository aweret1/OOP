a = [1,2,3,4,5,6,7,8,9]
del a[0]
del a[7]
print(a)

s = ''
while True:
    s = int(input('Число зі списку '))
    a.remove(s)
    print(a)
    if a == []:
        print('Вже нема чисел')
        break
        


    


        
    
