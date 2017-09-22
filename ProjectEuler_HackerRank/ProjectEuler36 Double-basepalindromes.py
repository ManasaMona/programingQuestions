def checkPalindrome(value):
    value = str(value)
    revValue= value[::-1]
    if(value == revValue):
        return True
    return False

def tobseK(num,bas):
    res1=""
    while(num>0):
        rem=num%base
        res1=res1+str(rem)
        num=num//base
    #print(res1)
    return res1
    


array = input().split(" ")
#print(array[0])
#print(array[1])

belowRange= int(array[0])
base=int(array[1])
res=0
for i in range(0,belowRange):
    if(checkPalindrome(i)==True and checkPalindrome(tobseK(i,base))==True): 
        res=res+i
print(res)
