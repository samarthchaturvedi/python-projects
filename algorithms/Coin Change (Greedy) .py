# Minimum coins using greedy approach

coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter amount: "))

coins.sort(reverse=True)

count = 0
used = []

for coin in coins:
    while amount >= coin:
        amount -= coin
        count += 1
        used.append(coin)

print("Coins used:", used)
print("Total coins:", count)