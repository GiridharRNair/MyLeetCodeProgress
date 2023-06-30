class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = list()
        out.append([1])
        for i in range(numRows - 1):
            row = [1]
            for j in range(i):
                row.append(out[i][j] + out[i][j+1])
            row.append(1)
            out.append(row)
        return out