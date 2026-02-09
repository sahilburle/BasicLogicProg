
abc = 0

print ("Enter the value of n :")
n = int(input())

for total in range (1,n) :
    abc = abc + total
print (abc)

"""
other below ways

num = 5
print(int(num*(num+1)/2))
...........................


def getSum(num):
  if num == 1:
    return 1
  return num + getSum(num-1)

num = 5
print(getSum(num))


"""