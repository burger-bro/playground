from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: 
            return [1]*numRows
        elif numRows == 2:
            return [[1], [1,1]]
        rows = [[1], [1,1]]
        numRows -= 2
        while numRows:
            row = [1] + [rows[-1][i] + rows[-1][i+1] for i in range(len(row)-1)] + [1]
            rows.append(row)
            numRows -= 1
        return rows