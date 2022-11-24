class Solution:
    def sortArray(self, num: List[int]) -> List[int]:
        if len(num) <= 1:
            return num
        elem = nums[0]
        l = [x for x in num if x < elem]
        mid = [x for x in num if x == elem]
        r = [x for x in num if x > elem]
        return self.sortArray(l) + mid + self.sortArray(r)