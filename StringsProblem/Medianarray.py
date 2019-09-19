nums1=[1,3]
nums2=[2]
def findMedianSortedArrays(self, nums1, nums2):
    result1 = []
    for i in range(len(nums1)):
        result1=result1.append(nums1[i])
    for i in range(len(nums2)):
        result1=result1.append(nums2[i])
    result1 = result1.sort()
    resultlen = len(result1)
    mid = resultlen / 2
    if resultlen % 2 == 0:
        print((result1[mid] + result1[mid - 1]) / 2)
    print(result1[mid])