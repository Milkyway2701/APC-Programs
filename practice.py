str=input("enter string :" )
left=0
right=len(str)-1
while left<right:
    if(str[left]==str[right]):
        print("Pallindrome")
    else:
        print("Not pallindrome")
    left+=1
    right-=1
    break


    
    