def solve(nums):
    n=len(nums)
    ans=[]
    for i in range(n):
        l=nums[i]-((i%7)*3)
        
        if (nums[i]%11==0):
            l+=nums[i]/11
        ans.append(l)   
   
    return ans
    
nums=list(map(int,input().split()))
a=solve(nums)
f=int(sum(a))
print(f)

     
    