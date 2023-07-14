 # Leetcode-39 Combination Sum

arr = list(map(int,input().split()))
target = int(input())
res = []
def combinationSum(idx, target, n, ds, arr):
    if idx == n:
        if target == 0:
            res.append(ds.copy())
            # print(ds)
        return

    if arr[idx] <= target  :
        ds.append(arr[idx])
        combinationSum(idx, target-arr[idx], n, ds, arr)
        ds.pop()
    
    combinationSum(idx+1, target, n, ds, arr)

combinationSum(0, target, len(arr), [], arr)
print(res)
