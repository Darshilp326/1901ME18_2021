def meraki_solve(i):
    if(i<10):
        return True
    else:
        x=i
        last=x%10
        x=x//10
        flag=False        
        while(x>0):
           y=x%10
           if(abs(y-last)==1):
               x=x//10
               last=y 
           else:
               flag=True
               break
        if(flag):
            return False 
        else:
          return True   

input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
meraki=0
non_meraki=0
for i in input:
    if(meraki_solve(i)):
        meraki+=1
        print('YES',i,'is a meraki number')
    else:
        non_meraki+=1
        print('NO',i,'is not a meraki number')

print("the input list contains", meraki, "meraki numbers and", non_meraki, "non meraki numbers.")        