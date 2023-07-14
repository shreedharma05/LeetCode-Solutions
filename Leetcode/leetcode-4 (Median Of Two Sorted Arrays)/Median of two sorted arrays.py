nums1 = []
nums2 = []

def findMedianSortedArrays(nums1,nums2):
    i,j = 0,0
    arr = []
    n1 = len(nums1)
    n2 = len(nums2)
    while i <= n1-1 and j <= n2-1:
        if nums1[i] < nums2[j]:
            arr.append(nums1[i])
            i += 1
        else:
            arr.append(nums2[j])
            j += 1
    while i < n1:
        arr.append(nums1[i])
        i+= 1
    while j < n2:
        arr.append(nums2[j])
        j += 1
            
    if len(arr)%2 == 0: return(arr[len(arr)//2] + arr[(len(arr)//2)-1])/2
    else: return arr[(len(arr)//2)]

print(findMedianSortedArrays(nums1,nums2)
