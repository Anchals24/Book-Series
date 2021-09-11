#3_Sum 

# Approach 1 : Brute-Force #TC : O(n***3)

A = [1 , 2, 3,1 ,2 ,3]
Target = 6
leng = len(A)
sett = set()
for i in range(leng): #O(n)
    for j in range(i+1 , leng): #O(n-1)
        for k in range(j+1 , leng): #O(n-2)
            if A[i]+ A[j]+ A[k] == Target:
                sett.add((A[i] , A[j] , A[k]))
print(sett)


#Approach 2 : Brute-Force #TC : O(n***3)

Arr = [3 , 1, 2, 8, 5]
Target = 10
l = len(Arr)
D = {}
for a in range(l): #O(n)
    for b in range(a+1 , l):
        D[(a , b)] = Arr[a] + Arr[b]
print(D)
for key , values in D.items(): #O(n**2)
    l = 0
    for a in Arr: #O(n)
        storingkey = key
        if D[key] + a == Target:
            if a != Arr[storingkey[l]] and a != Arr[storingkey[l+1]]:
                ANS = (a , Arr[storingkey[l]] , Arr[storingkey[l+1]])
                print(ANS)
        break
        
def three_sum(A):
    target = 55 #O(1)
    A.sort() #O(nlogn)
    leng = len(A) #O(n)                     
    for a in range(leng): #O(n)
        i = a + 1
        j = leng - 1 
        while i < j: #O(n-2) times
            if A[a] + A[i] + A[j] > target: #O(1)
                j -= 1                      #O(1)
            elif A[a] + A[i] + A[j] < target: #O(1)
                i += 1                        #O(1)
            elif A[a] + A[i] + A[j] == target: #O(1)
                return (A[a] , A[i] , A[j])    #O(1)
    return "Does not exist"
print(three_sum([ 1 , 1, 0, 5, 7, 6]))
   
#O(n**n)
   

        

