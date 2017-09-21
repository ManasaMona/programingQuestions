import math  
primeList = []
resList=[]

def isPrime(num):
    if(num==2):
        return True
    if(num%2==0):
        return False
    flag = True
    end =int(math.sqrt(num))+1
    
    for i in range(2,end): 
            if(num%i==0):
                flag = False
                break
    return flag

def rotate(num):
    toString = str(num)
    if(len(toString)==1):
        resList.append(num)
    elif(len(toString)==2):
        newString = toString[1]+toString[0]
        prime=isPrime(int(newString))
        if(prime):
            resList.append(num)
    else:
        lengthofStr=len(toString)
        all= True
        for k in range(lengthofStr):
            newString =toString[1:]+toString[0]
            prime = isPrime(int(newString))
            if(prime):
                toString = newString
                continue
            else:
                all=False
        if(all):
            resList.append(num)
    

inputRange = int(input())

for i in range(2,inputRange):
    prime=isPrime(i)
    if(prime):
        primeList.append(i)
for k in primeList:
    rotate(k)

resSum=0
for j in resList:
    resSum=resSum+j
print(resSum)