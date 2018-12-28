class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i] = A[i][::-1]
            for k in range(len(A[i])):
                A[i][k] = A[i][k]^1
        return A


class Solution2_BuNB:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        ret = []
        for l in A:
            ret.append([x ^ 1 for x in l[::-1]])
        return ret
