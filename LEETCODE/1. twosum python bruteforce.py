class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for countx, x in enumerate(nums):
            for county, y in enumerate(nums):
                if x+y == target and countx != county:
                    expected = [countx, county]
                    return(expected)