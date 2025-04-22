n = int(input())
tips = [int(input()) for _ in range(n)]

tips.sort(reverse=True)

sum = 0
for i in range(n):
    sum += tips[i] - i if (tips[i] - i) > 0 else 0

print(sum)
