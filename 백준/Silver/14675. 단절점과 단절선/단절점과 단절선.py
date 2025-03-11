import sys

input = sys.stdin.readline

# N 정점개수
n = int(input())
tree = [[] for _ in range(n + 1)]

# 간선 정보 저장 배열 (2번 질의를 위함)
edges = []
# N-1개만큼 간선정보 a,b출력
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    edges.append((a, b))
# q 질의의 개수
q = int(input())
# 질의 t k t==1 단절점 t==2 단절선
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        # 트리에서는 연결된 노드가 2개 이상이면 단절점 (루트 노드 제외)
        # 루트 노드는 자식이 2개 이상일 때만 단절점
        if len(tree[k]) >= 2:
            print("yes")
        else:
            print("no")
    else:
        print("yes")
