class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        result = []
        while r >= l:
            r_v = nums[right] ** 2
            l_v = nums[left] ** 2
            if r_v >= l_v:
                result.append(r_v)
                r -= 1
            else:
                result.append(l_v)
                l += 1
        return result[::-1]