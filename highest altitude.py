class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        op = [0]
        for i in range(len(gain)):
            op.append(op[i] + gain[i])
        
        maximum = max(op)
            
        return maximum
    
