#3_Sum 

# Approach 1 : Brute-Force

A = [1 , 2, 3,1 ,2 ,3]
Target = 6
leng = len(A)
sett = set()
for i in range(leng):
    for j in range(i+1 , leng):
        for k in range(j+1 , leng):
            if A[i]+ A[j]+ A[k] == Target:
                sett.add((A[i] , A[j] , A[k]))
print(sett)


#Approach 2 : Brute-Force

Arr = [3 , 1, 2, 8, 5]
Target = 10
l = len(Arr)
D = {}
for a in range(l):
    for b in range(a+1 , l):
        D[(a , b)] = Arr[a] + Arr[b]
print(D)
for key , values in D.items():
    l = 0
    for a in Arr:
        storingkey = key
        if D[key] + a == Target:
            if a != Arr[storingkey[l]] and a != Arr[storingkey[l+1]]:
                ANS = (a , Arr[storingkey[l]] , Arr[storingkey[l+1]])
                print(ANS)
        break
        
   
