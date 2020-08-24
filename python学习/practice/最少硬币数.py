def min_corn(coins, amount):
    dp = [amount + 1] * (amount + 1)
    # // base case
    dp[0] = 0;
    i = 0
    while i < len(dp):
        for coin in coins:
            if i - coin < 0:
                continue;# // ⼦问题⽆解，跳过
            dp[i] = min(dp[i], 1 + dp[i - coin])# // 内层 for 在求所有⼦问题 + 1 的最⼩值
        i += 1
    return -1 if dp[amount] == amount + 1 else dp[amount]; 
    
print(min_corn([1,2,5], 5))