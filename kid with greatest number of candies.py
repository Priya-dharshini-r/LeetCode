# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: 
# Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids. 
# Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
# Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
# Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
# Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
      # Define max as zero and add extracandies to the initial list and add it to maximum candies list.
        max = 0
        maximum_candy_list = []
        for i in range(len(candies)):
            maximum = extraCandies + candies[i]
            maximum_candy_list.append(maximum)
            # finiding maximum in the candies list.
            if candies[i] > max:
                max = candies[i]
                
        return_list = []
        
        for i in range(len(maximum_candy_list)):
          # if any element in the maximum candies list is maximum 
            if maximum_candy_list[i] >= max:
                return_list.append(True)
            else:
                return_list.append(False)
        return return_list
