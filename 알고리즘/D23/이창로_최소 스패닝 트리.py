import heapq
T = int(input())

def make_set(x):
    p[x] = x

def find_set(x):
    if x == p[x]:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x, y):
    py = p[find_set(y)]
    px = p[find_set(x)]
    if px > py:
        p[py] = px
    else:
        p[px] = py

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = [list(map(int, input().split())) for i in range(E)]

    for i in range(E):
        print(adj[i])
    # 간선을 간선가중치를 기준으로 정렬
    adj.sort(key=lambda x: x[2])
    
    # make_set: 모든 정점에 대해 집합 생성
    # 모든 간선에 대해서 반복 -> V-1개의 간선이 선택될 때 까지
    # 사이클이면 스킵 : 간선의 두 정점이 서로 같은 집합이면 => find_set
    # 간선 선택
    # => mst에 간선 정보 더하기 / 두 정점 합치기 => union


    INF = float('inf')
    key = [INF] * V
    mst = [False] * V
    pq = []
    key[0] = 0
    p = [i for i in range(V+1)]
    heapq.heappush(pq, (0,0))
    print(p)
    # while pq:
        # k, node = heapq.heappop(pq) # 우선순위가 가장 높은 것을 가져옴
        # mst[node] = True
        # for dest, wt in adj[node]:
        #     if not mst[dest] and key[dest] > wt:
        #         key[dest] = wt
        #         heapq.heappush(pq, (key[dest], dest))
