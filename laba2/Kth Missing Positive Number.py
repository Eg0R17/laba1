class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)
        while r - l > 0:
            mid = l + (r - l) // 2
            if arr[mid] - (mid + 1) >= k:
                r = mid
            else:
                l = mid + 1
        return l + k