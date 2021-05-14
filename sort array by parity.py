# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

class Solution:
  def sortArrayByParity(self, A: List[int]) -> List[int]:
        array = []
        array2 = []
        for i in A:
            if i%2 == 0:
                array.append(i)
            else:
                array2.append(i)
                
        return array + array2
    
