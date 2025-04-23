n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

count = 0
for c in reversed(coins):
    if k // c > 0:
        count += k // c
        k %= c

print(count)
