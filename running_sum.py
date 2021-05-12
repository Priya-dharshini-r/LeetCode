# input = [1,2,3,4] --> output = [1,3,6,10]

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Assign an empty list and initialize sum to zero.
        return_list = []
        sum = 0
        # for each element in the num list add each element to the sum.
        for i in range(len(nums)):
            sum = sum + nums[i]
            # add sum to the return list and return it
            return_list.append(sum)
        return return_list
