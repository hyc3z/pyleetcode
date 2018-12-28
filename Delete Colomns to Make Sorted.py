class Solution:
    def minDeletionSize(self,A):
        """
        :type A: List[str]
        :rtype: int
        """
        length = len(A[0])
        delq = [0]*length
        for i in range(length):
            for j in range(len(A)-1):
                if A[j][i]>A[j+1][i]:
                    delq[i] = 1
        return delq.count(1)




A = ["abcdef","uvwxyz"]
