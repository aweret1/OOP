from collections import Counter

a = {2:5, 5:3, 7:4, 10:4, 8:7, 3:2, 0:0, 1:9}

def sort(dic):
    lis = [(k, dic[k]) for k in sorted(dic.keys(), key=dic.get, reverse=False)]
    return lis 

new_a = sort(a)
print(new_a)


def sort_dic(d):
    l = [(k, d[k]) for k in sorted(d.keys(), key=d.get, reverse=True)]
    return l

new_b = sort_dic(a)
print(new_b)

z = Counter(new_a)+Counter(new_b)
print(z)


