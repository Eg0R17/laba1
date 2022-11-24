class Solution:
    def peakIndexinMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while r - l > 1:
            mid = l + (r - l) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid] > arr[mid + 1]:
                r = mid
            else:
                l = mid