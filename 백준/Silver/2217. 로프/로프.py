n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort()

max_weight = 0
for i in range(len(ropes)):
    max_weight = max(ropes[i] * (n - i), max_weight)

print(max_weight)