dp = [0 for i in range(1000001)]
N = int(input())

dp[1] = 1
dp[2] = 2

for i in range(3, 1000001):
  dp[i] = (dp[i-1] + dp[i-2] ) % 15746
print(dp[N] % 15746)