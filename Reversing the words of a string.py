#Without using Array or any function.

S = " Sky is     Blue   "
temp = ""
final = ""
for s in range(len(S)-1 , -1 , -1):
    if S[s] != " ":
        temp += S[s]
    if len(temp) > 0 and S[s] == " ":
        for t in range(len(temp)-1 , -1 , -1):
            final += temp[t]
        final += " "
        temp = ""
print( "Original String is >>" , S)
print("After reversing the words , string is >>" ,final)
#The above solution is not a correct solution. Getting stuck on a single case. Need to re-write the code.


#Using functions and array

String = "Sky is Blue"
String = String.split()
String.reverse()
Final = ""
for s in String:
    Final += s 
    Final += " "
print(Final)


        
    

        


