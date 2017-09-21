import math
inputValue = int(input())
def checkDivide(one,two):
    if(one%two==0):
        return True
    return False
if(inputValue>9):
    finalAns=0
    for i in range(10,inputValue):
        add=0
        temp = i
        temp2=i
        while(temp>0):
            reminder = int(temp%10)
            add = add+ math.factorial(reminder)
            temp=temp/10
        toAdd= checkDivide(add,temp2)
        print("Add:",add,"NUm : ",temp2,"boolean",toAdd)
        if(toAdd):
            finalAns=finalAns+temp2
    print(finalAns)
    