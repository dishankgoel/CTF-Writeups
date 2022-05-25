from pwn import *

p = remote("tjc.tf", 31111)


def djiktra(graph, start, end):
    n = len(graph)
    dp = [10**18 for i in range(n)]
    dp[start] = 0
    found = [start]
    found_map = {}
    for i in range(n):
        found_map[i] = 0
    found_map[start] = 1
    while len(found) != n:
        min_cost = 10**18
        new_v = None
        for u in found:
            for v in range(n):
                if graph[u][v] != -1 and not found_map[v]:
                    cost = dp[u] + graph[u][v]
                    if cost < min_cost:
                        min_cost = cost
                        new_v = v
        if min_cost == 10**18 or new_v is None:
            break
        found.append(new_v)
        found_map[new_v] = 1
        dp[new_v] = min_cost
    if dp[end] == 10**18:
        return -1
    else:
        return dp[end]


def parse_msg(msg):
    routes_string = msg.split(b"routes:\n")[-1].split(b"\nAndrew")[0]
    routes = [[int(a) for a in i.split()] for i in routes_string.split(b"\n")]
    print(routes)
    assert(len(routes) == 40)
    graph = [[-1 for i in range(21)] for j in range(21)]
    for row in routes:
        graph[row[0]][row[1]] = row[2]
        graph[row[1]][row[0]] = row[2]
    ans = djiktra(graph, 0, 20)
    print("Answer found: ", ans)
    return ans

for i in range(50):
    print("[*] Test number: ", i + 1)
    msg = p.recvuntil(b"answer: ")
    ans = parse_msg(msg)
    p.sendline(str(ans))

p.interactive()
