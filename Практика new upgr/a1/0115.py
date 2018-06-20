summa = 0
count=0
while True:
    s = int(input("Число "))
    summa += s
    count += 1
    if s == 0:
        break

if count != 1:
    print(summa/(count-1))
else :
    print("Error")
                            
    

    


    
