class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        my_dict = {}
        for i in range(lowLimit, highLimit+1):
            sum = 0
            for num in str(i):
                sum += int(num)
                
            if sum in my_dict:
                my_dict[sum] += 1
            else:
                my_dict[sum] = 1
                
        output = max(my_dict.values())
        return output
