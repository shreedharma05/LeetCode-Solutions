# arr = [1,1,1,2,2]
arr = [10,1,2,7,6,1,5]
arr.sort()
n = len(arr)
res = []
def combinationSum2(idx,target,arr,n,ds,res):
    if target == 0:
        res.append(ds.copy())
        return
    
    for i in range(idx,n):
        if i>idx and arr[i] == arr[i-1]: continue
        if arr[i]>target: break

        ds.append(arr[i])
        combinationSum2(i+1,target-arr[i],arr,n,ds,res)
        ds.pop()

combinationSum2(0,8,arr,n,[],res)
print(res)
