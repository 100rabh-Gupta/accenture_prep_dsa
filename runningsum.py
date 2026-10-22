def solve(n):
    rsum=0
    count=0
    for i in range(1,n+1):
        rsum+=i
        if(rsum%5==0):
            count+=1
    print(f"count = {count}")
    print(f"running sum = {rsum}")


n=int(input())
solve(n)