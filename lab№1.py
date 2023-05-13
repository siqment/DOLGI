# 1
a = [1, 2, 3, 4, 5]
print(a[0], a[2], a[-2])

#2
a=[1,2,3,4,5,6,7,8,9]
N=int(input())
if N<=len(a):
    print(a[N]**N)
else:
    print(-1)

# 3
a='xcfvbfnjh'
s='f'
k=0
for i in range (0, len(a)):
    if a[i]==s:
        k+=1
    if k==2:
        print(i)
        break

# 4
number = '101100110100'
number = number[::-1]
print(number)
count = 0
for n in number:
    if n == '0':
        count += 1
    else:
        break
print(count)

#5
n = input()[::-1]
print(n)

#6
b = [0, 0, 0, 0, 0]
b = input()
check = False
for i in range(0, len(b)-1):
    if b[i] == b[i+1]:
        check = True
    else:
        check = False
        break
print(check)

#7
i=str(input())
while len(i)<16:
    i=input()

a,b,c,d=False,False,False,True
for e in i:
    if e.isupper(): a=True
    elif e.islower(): b=True
    elif e.isnumeric(): c=True
    else: d=False
if a and b and c and d:
    print('Безопасный пароль')
else:
    print('Небезопасный пароль')

#8
def z(arr):
    for i in arr:
        if type(i) is list:
            z(i)
        else:
            print(i,end=' ')
    return

a=[8,[6,4],[7,[1,9]]]
z(a)

#9
def max_key(dict):
    print('Словарь: ', dict) #вывод словаря {'a': 6, 'b': 8, 'c': 1, 'd': 120}
    print('Ключ максимального значения в словаре: ', max(dict, key=dict.get)) # возвращает максимальное значение ключа из словаря
max_key({'a': 6, 'b': 8, 'c': 1, 'd': 120})

#10
def foo(a):
    b = []
    for x in a:
        if a.count(x)>1:b.append(x)
    return b

print(foo([2, 3 ,3 ,5, 4, 2]))

