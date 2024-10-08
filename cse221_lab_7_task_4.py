
def min_coins(coins, target_amount):

    min_coins_needed = [float('inf')] * (target_amount + 1)
    min_coins_needed[0] = 0

    for coin in coins:
        for j in range(coin, target_amount + 1):
            min_coins_needed[j] = min(min_coins_needed[j], min_coins_needed[j - coin] + 1)

    if min_coins_needed[target_amount] == float('inf'):
        return -1
    else:
        return min_coins_needed[target_amount]

inputfile = open("input4.txt", "r")
outputfile = open("output4.txt", "w")
v = inputfile.readlines()

N, target_amount = map(int, v[0].strip().split(" "))
coins = list(map(int, v[1].strip().split(" ")))

outputfile.write(str(min_coins(coins, target_amount)))
outputfile.close()