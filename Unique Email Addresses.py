class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        a = set()
        for i in emails:
            q = i.split('@')
            a.add((q[0].split('+'))[0].replace('.','')+q[1])
        return(a.__len__())
