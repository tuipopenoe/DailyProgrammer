# Tui Popenoe
# Challenge121E.py - Bytelandian Exchange I

def bytelandianExchange(coins):
    divs = [2, 3, 4]
    change = list()
    for i in coins:
        change.append(int(i / m) for m in divs)

    if coins[0] == 0:
        return len(change)
    return len(change) + for k in change: bytelandianExchange(k)