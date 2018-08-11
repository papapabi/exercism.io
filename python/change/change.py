from math import inf


def find_minimum_coins(total_change, coins):
    if total_change < 0:
        raise ValueError(f'total_change cannot be < 0: \
                         find_minimum_coins({total_change}')
    # List containing the min number of coins to make N cents.
    # min_coins_for[1] = {min number of coins to make 1 cent}
    min_coins_for = [inf] * (total_change + 1)
    # List containing the coin last used to reach N cents.
    coins_used = [-1] * (total_change + 1)

    min_coins_for[0] = 0
    for _, coin in enumerate(coins):
        for j, _ in enumerate(min_coins_for):
            if j >= coin:
                if min_coins_for[j - coin] + 1 < min_coins_for[j]:
                    min_coins_for[j] = 1 + min_coins_for[j - coin]
                    coins_used[j] = coin

    possible_coins = []
    while total_change > 0:
        if coins_used[total_change] == -1:
            raise ValueError("no combination adds up to target")
        possible_coins.append(coins_used[total_change])
        total_change -= coins_used[total_change]
    return sorted(possible_coins)
