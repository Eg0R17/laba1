class Solution:
    def searchInsertpostion(self, num, target):
        if not num:
            return 0
        l = 0
        r = len(num)
        while l < r:
            mid = (l + r) // 2
            if target > num[mid]:
                l = mid + 1
            else:
                r = mid
        return left