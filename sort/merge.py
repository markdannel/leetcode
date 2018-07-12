def merge(nums1, m, nums2, n):
    def move(nums, i, n):
        k = len(nums)-1
        while k > i:
            nums[k] = nums[k-1]
            k -= 1
        nums[i] = n

    i = j = 0
    while i < m and j < n:
        if nums1[i] > nums2[j]:
            move(nums1, i, nums2[j])
            #i += 1
            m += 1
            j += 1
        i += 1

    while j < n:
        move(nums1, i, nums2[j])
        i += 1
        j += 1
    print(nums1)

    # nums1 = nums1[:m]
    # i = j = 0
    # while i < len(nums1) and j < n:
    #     if nums1[i] >= nums2[j]:
    #         nums1.insert(i, nums2[j])
    #         i += 1
    #         j += 1
    #     i += 1

    # while j < n:
    #     nums1.insert(i, nums2[j])
    #     i += 1
    #     j += 1
    # print(nums1)
# nums1 = [4,5,6,0,0,0]
# nums2 = [1,2,3]
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1,3,nums2,3)
