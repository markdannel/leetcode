nums1 = [1, 2, 2, 1]
nums2 = [2,2]

nums1 = sorted(nums1)
nums2 = sorted(nums2)

l1 = len(nums1)
l2 = len(nums2)
i = j = 0
target = []


while j < l2 and i < l1:
    if nums1[i] == nums2[j]:
        target.append(nums1[i])
        i += 1
        j += 1
    elif nums1[i] > nums2[j]:
        j += 1
    else:
        i += 1
print(target)
#return target

