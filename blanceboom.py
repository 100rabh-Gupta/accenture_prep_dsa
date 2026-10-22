def blanceboom(input1,input2):
    n=input1
    arr=input2
    frq={}
    for i in arr:
        frq[i]=frq.get(i,0)+1
        
    small=0
    greater=0
    equal=0
    ans=0
    found =False
    for x in sorted(frq):
        equal=frq[x]
        greater=n-equal-small
        
        if(greater==small and equal<=2):
            ans+=x*equal
            found=True
          
        
        small+=equal
    if(found):
        return ans
    else:
        return sum(arr)

n=int(input())
arr=list(map(int,input().split()))
print(blanceboom(n,arr))