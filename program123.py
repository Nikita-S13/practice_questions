#Write a function to tell user if he/she is able to vote or not.`( Consider minimum age of voting to be 18. )`
def vote(x):
    if x>=18:
        print('You are able to vote')
    else:
        print('You are not able to vote')
age=int(input("enter the age:"))
vote(age)