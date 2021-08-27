#Bookseries : Ques2
#Which element in array is repeating maximum times?

#Approach1 : Time Complexity : O(n ** 2)  , Space Complexity : O(1)
A = [ 1 , 2, 1, 3, 1, 2, 4 ,5]
counter = 0
maxcounter = 0
candidate = A[0]
l = len(A)
maxcountelement = A[0]
for i in range(l):
    candidate = A[i]
    counter = 1
    for j in range(i+1 , l):
        if A[i] == A[j]:
            counter += 1
    if (counter > maxcounter):
        maxcounter = counter
        maxcountelement = A[i]
print(maxcounter)
print(maxcountelement)

#Approach2 : Using sort
#Time complexity : O(nlogn)
A = [ 1 , 2, 1, 3, 1, 2, 4 ,5]
A.sort()
l = len(A)
maxrepeatingele = A[0]
currele = A[0]
count = 1
maxcount = 1
for i in range(1 , l):
    if A[i] == currele:
        count += 1
    else:
        currele = A[i]
        count = 1
    if count > maxcount:
        maxcount = count
        maxrepeatingele = currele
print("Element which is getting repeated maximum times is >> " , maxrepeatingele, "and its maximum count is >> " , maxcount )




