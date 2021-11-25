#https://leetcode.com/problems/pascals-triangle-ii/submissions/
#재귀로 풀이

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            turn = rowIndex -1
            li = Solution.getRow(self, turn)
            rowli = [1]
            for i in range(turn):
                rowli.append(li[i]+li[i+1])
            rowli.append(1)
            return rowli
