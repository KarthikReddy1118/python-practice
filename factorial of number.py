a=int(input("enter number to  find a factorial:"))
ans=15

if a==0:
    print(1)
elif a<0:
    print("error occured")
else:
    for i in range(1,a+1):
        ans=ans*i
print(ans)

#factorial of 0 is 1
""" factoraial of negative numbers are not defined"""
"if string is not assigned to a variable means it will become a comment line "       
# 1*2*3 ==3*2*1 
#a+1 because range last number not included
