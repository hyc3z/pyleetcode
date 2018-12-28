import time
def repeatedNTimes(A):
    """
    :type A: List[int]
    :rtype: int
    """
    for i in A:
        if A.count(i) == A.__len__()>>1:
            return i

def nb(A):
    return (sum(A) - sum(set(A))) // (len(A) - len(set(A)))

q = [1,2,3,3]
t1 = time.process_time_ns()
print(repeatedNTimes(q))
t2 = time.process_time_ns()
print(t2-t1)

t1 = time.process_time_ns()
print(nb(q))
t2 = time.process_time_ns()
print(t2-t1)