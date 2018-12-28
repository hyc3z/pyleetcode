from collections import deque

def deckRevealedIncreasing(deck):
    """
    :type deck: List[int]
    :rtype: List[int]
    """
    length = len(deck)
    deck.sort()
    biggest_card = deck.pop()
    dq = collections.deque()
    dq.appendleft(biggest_card)
    for i in range(length - 1):
        dq.appendleft(dq.pop())
        dq.appendleft(deck.pop())
    return dq


def deckRevealedIncreasing2(deck):
    """
    :type deck: List[int]
    :rtype: List[int]
    """
    length = len(deck)
    deck.sort()
    biggest_card = deck.pop()
    dq = []
    dq.append(biggest_card)
    for i in range(length-1):
        p = dq.pop()
        dq = [deck.pop()]+[p]+dq
    return dq

# I wrote both of the functions.
deck = [17,13,11,2,3,5,7]
print(deckRevealedIncreasing2(deck))