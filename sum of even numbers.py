n=int(input("enter a number to find sum of even in  that number:"))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum=sum+i
print(sum)

# printing the sum of even numbers in that number
# like we give 6 
#out put was 12 because 2+4+6=12