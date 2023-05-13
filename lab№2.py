#1
def fibonacci(i):
    if i in (1,2):
        return 1
    return fibonacci(i-1) + fibonacci(i-2)
print(fibonacci(6))

#2
def remove_common(a, b):
    for i in a[:]:
        if i in b:
            a.remove(i)
            b.remove(i)
    print('Список 1 : ', a)
    print('Список 2 : ', b)

if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    b = [4,5,6,7,8,9]
    remove_common(a, b)

#3
def function(nums,):
    b=[]
    for i in nums:
        if nums.count(i)>=4:
            b.append(i)
    print(b)
function([1,2,3,3,3,3,3])

#4
def nestsum(lst):
    nest_list = []
    for item in lst:
        if isinstance(item, list) or isinstance(item, tuple):
            nest_list.append(sum(flatten(item)))
        else:
            nest_list.append(item)
    return nest_list
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list) or isinstance(item, tuple):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list
n = [1, 2, [3, 4], [2, 5, [3, 4, [5]]]]
print(n, '->', nestsum(n))

#5
def sequence(lst): 
    if len(lst) == 1:
        return lst
    temp, save = [], [] 
    for i in range(len(lst) - 1):
        if lst[i + 1] > lst[i]:
            temp.append(lst[i]) if temp == [] else temp
            temp.append(lst[i + 1])
            if len(save) <= len(temp):
                save = temp
        else:
            temp = []
    return save

s = [1, 2, 3, 2, 4, 5, 6, 7]
print(s, ' ->', sequence(s))

#6
def function(text):
    count = [i for i in range(len(text))]
    print(''.join(text[i].upper() if (i%2 != 0) else text[i] for i in count))

text = input()
function(text)

#7
n=int(input())
for i in range(0,n+1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
if i==n:
    for i in range(n-1,0,-1):
        for j in range(0,n-i):
            print(end=" ")
        for j in range(0,i):
            print("*",end=" ")
        print()

#8
def matrix(num):
    mat = [[0 for i in range(num)] for j in range(num)]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i == 0 or j == 0:
                mat[i][j] = 1
            else:
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j]," ", end='')
        print( sep=", ")
matrix(5)


#9
def findSum(str1):
    temp = '0'
    Sum = 0

    for c in str1:
        if (c.isdigit()):
            temp += c
        else:
            Sum += int(temp)
            temp = '0'
    return Sum + int(temp)
str1 = '54 мрм5 56'
print(findSum(str1))

#10
import re
def string_sum(text):
    temp = []
    result = []
    keys, values = range(48, 58), range(0, 10)
    nums = dict(zip(keys, values))

    for i in re.findall('\d+', text):
        for j in i:
            if ord(j) in nums:
                temp.append(nums[ord(j)])
        temp = sum(10 ** i[0] * i[1] for i in enumerate(reversed(temp)))
        result.append(temp)
        temp = []
    return sum(result)

string_sum('175 конфет и 84 леденца')
