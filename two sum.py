class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        for i in range(0,len(nums)):
            if len(result)==2:
                break
            for j in range(0,len(nums)):
                if nums[i]+nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result
        
