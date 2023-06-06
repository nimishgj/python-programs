def Palindrome(x):
    lst=[]
    while x:
        lst.append(x%10)
        x=x//10
    return lst==lst[::-1]


y=Palindrome(1221)
print(y)