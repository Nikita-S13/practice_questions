for num in range(1,100000):
    pow=len(str(num))
    temp=num
    total=0
    while num>0:
        digit=num%10
        total+=digit**pow
        num=num//10
    if temp==total:
        print(temp,end=',')