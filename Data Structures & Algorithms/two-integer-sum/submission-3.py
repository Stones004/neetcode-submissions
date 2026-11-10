class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1) :
            diff = target-nums[i]
            print("Diff : ",diff)
            for j in range(i+1,len(nums)) :
                if diff == nums[j] :
                    return [i,j]
        
