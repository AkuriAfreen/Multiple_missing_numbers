nums=list(map(int,input().split()))
set_nums=[]
for i in range(1,max(nums)+1):
    if i not in nums:
        set_nums.append(i)
print("missing numbers:",set_nums)