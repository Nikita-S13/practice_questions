#wap to create a list of 50 prime numbers
prime_num=[]
for num in range(1,51):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            prime_num.append(num)
print(prime_num)