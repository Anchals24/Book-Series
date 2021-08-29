#Question >>> Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

#Brute-Force Method
A = "A man, a plan, a canal: Panama"
lowerstring = A.lower()
NewS = ""
Alphanumeric = ["a" , "s" , "d" , "f" , "g" , "h" , "j" , "k" , "l" , "z" , "x" , "c" , "v" , "b" , "n" , "m" , "q" , "w" , "e" , "r" , "t" , "y" ,"u" , "i" , "o" , "p" , "1" , "2" , "3" , "4" , "5" , "6","7","8 ", "9" ,"0" , 0 , 9 , 8 , 7 , 6 , 5 , 4 ,3, 2 , 1]
for s in lowerstring:
    if s in Alphanumeric:
        NewS += s
reversestr = ""
l = len(NewS) -1
for n in range(l , -1 , -1):
    reversestr += NewS[n]
if reversestr == NewS:
    print(1)
else:
    print(0)

#Using Two-Pointer
def isPalindrome(A):
        lowerstring = A.lower()
        Alphanumeric = ["a" , "s" , "d" , "f" , "g" , "h" , "j" , "k" , "l" , "z" , "x" , "c" , "v" , "b" , "n" , "m" , "q" , "w" , "e" , "r" , "t" , "y" ,"u" , "i" , "o" , "p" , "1" , "2" , "3" , "4" , "5" , "6","7","8 ", "9" ,"0" , 0 , 9 , 8 , 7 , 6 , 5 , 4 ,3, 2 , 1]
        r = len(A) - 1
        l = 0
        while r >= l:
            if lowerstring[l] in Alphanumeric and lowerstring[r] in Alphanumeric:
                if lowerstring[l] != lowerstring[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            elif lowerstring[r] not in Alphanumeric:
                r -=1
            elif lowerstring[l] not in Alphanumeric:
                l += 1
        return True
print(isPalindrome("A man, a plan, a canal: Panama"))

#Fast Solution:
def isPalindrome(A):
        a = A.lower()
        sp = [",",".",":"," ",'"']
        for i in sp:
            a = a.replace(i,'')
        #print("A after removing special characters >>" , a)
        if (a == a[::-1]):
            return(1)
        else:
            return(0)
isPalindrome("A man, a plan, a canal: Panama")


#Functions : >> isalnum()
# Stripped String find out : re.sub(r'\W+','', S) [After importing the library >> "import re"]


        
    



