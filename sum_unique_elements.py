class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        my_dict = {}
        for i in nums:
            if i in my_dict:
                my_dict[i]+=1
            else:
                my_dict[i] = 1
        sum_unique = []
        for key, value in my_dict.items():
            if value<=1:
                sum_unique.append(key)
        result = sum(sum_unique)
        return result
          
# solution 2
# Using divide and conquer method

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = map(lambda x: x*x, nums)
        result = list(result)
        i = 0
        j = n-1
        final_list = []
        while i<=j:
            if result[i] > result[j]:
                final_list.append(result[i])
                i = i+1
            else:
                final_list.append(result[j])
                j = j-1
        final_result = final_list[::-1]
        return final_result
