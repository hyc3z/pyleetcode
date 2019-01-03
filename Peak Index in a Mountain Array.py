class Solution:
    def peakIndexInMountainArray(self, A):
        def gold1(l, r):
            return l + int(round((r - l) * 0.382))

        def gold2(l, r):
            return l + int(round((r - l) * 0.618))

        l, r = 0, len(A) - 1
        x1, x2 = gold1(l, r), gold2(l, r)
        while x1 < x2:
            if A[x1] < A[x2]:
                l = x1
                x1 = x2
                x2 = gold1(x1, r)
            else:
                r = x2
                x2 = x1
                x1 = gold2(l, x2)
        return x1
