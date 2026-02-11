print("Enter the number to check if it is prime :")
num = int(input())
flag = 0
i = 2

for i in range (2, num):
    if (num % i == 0):
       flag = 1
    break 
    
if (flag == 1) :
    print(f"{num} is not prime")
else :
    print(f"{num} is prime")