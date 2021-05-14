# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        i = 1
        result_sum = 0
        while i<=len(arr):
            j = 0
            while j<=(len(arr)) - i:
                result_sum += sum(arr[j:j+i])
                # add = sum(result)
                # result_sum += add
                
                j = j+1
            i = i+2
        return result_sum
            
        
    
