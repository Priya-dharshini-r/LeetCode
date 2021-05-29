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
          
