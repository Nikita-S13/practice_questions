#wap to generate a list of cricketers entered by user only if the first letter of the name is capital. the size will depend upon user.
n=int(input("enter the length of list:"))
list1=[]
for i in range(n):
    str=input('enter the cricketer name:')
    if str==str.title():
        list1.append(str)
print(list1)