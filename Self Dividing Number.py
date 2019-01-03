def selfDividingNumbers( left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    l = []
    for i in range(left, right + 1):
        flag = True
        for j in str(i):
            if j == '0':
                flag = False
                break
            if i % int(j) != 0:
                flag = False
                break
        if flag:
            l.append(i)
    return l