#Find a pair whose sum is equal to target!

#Approach1 : Brute-Force Method. 
#Time Complexity : O(n**2)

A = [ 1 , 2, 4, 4]
target = 8
l = len(A)
for i in range(l):
    for j in range(i+1 , l):
        if A[i] + A[j] == target:
            print((A[i] , A[j]))

#Aprroach2 : If its given in ascending order, We can also use Binary search. But, it will be taking O(nlogn)

#Approach3 : Two pointer
#Time complexity : O(n)
A = [ 1 , 2, 4, 4]
target = 8
i = 0
j = len(A) - 1
while (i < j):
    summ = A[i] + A[j]
    if summ < target:
        i += 1
    elif summ > target:
        j -= 1
    elif summ == target:
        print(True)
        i = j
        
#Using hashing....

Arr = [1 , 2, 4 , 4]
summ = 8
leng = len(Arr)
s = set()
for i in range(leng):
    temp = summ - Arr[i]
    if temp in s:
        print("The pair whose sum is equal to the target is " , (temp , Arr[i]))
    s.add(Arr[i])

