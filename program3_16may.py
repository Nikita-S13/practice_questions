#write a program to store all the armstrong number till 100000
for num in range(1,100001):
    sum=0
    temp=num
    while temp>0:
        rem=temp%10
        sum=rem**3
        temp=temp//10
        if num==sum:
            print(num)