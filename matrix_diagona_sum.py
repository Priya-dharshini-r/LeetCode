class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        primary_diagonal = []
        secondary_diagonal = []
        for i in range(n):
            primary_diagonal.append(mat[i][i])
        for i in range(n):
            secondary_diagonal.append(mat[i][n-i-1])
        final = primary_diagonal + secondary_diagonal
        result = sum(final)

        if n%2 == 1:
            position = math.floor(n/2)
            res = mat[position][position]
            
            sum_of_diagonal = result - res
            return sum_of_diagonal
        else:
            return result
