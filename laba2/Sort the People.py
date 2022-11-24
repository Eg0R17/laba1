class Solution:
    def sortThepeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = {}
        for i in range(0, len(names)):
            people[heights[i]] = names[i]
        heights.sort(key=lambda x: -x)
        list = []
        for item in heights:
            list.append(people[item])
        return list