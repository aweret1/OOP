l = []
while True:
    s = input('Слово для списку ')
    l.append(s)
    print(l)
    if s == '':
        l.remove('')
        print(set(l))
        break
