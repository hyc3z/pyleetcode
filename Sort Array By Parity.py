class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = []
        C = []
        for i in A:
            if i % 2 == 0:
                B.append(i)
            else:
                C.append(i)
        return B+C


class NBSolution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return [x for x in A if not x&1] + [x for x in A if x&1]
