"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]

Example 2:
Input: n = 2, connections = [[0,1]]
Output: [[0,1]]

Constraints:
- 2 <= n <= 10^5
- n - 1 <= connections.length <= 10^5
- 0 <= ai, bi <= n - 1
- ai != bi
- There are no repeated connections.
"""

from collections import defaultdict

def critical_connections(n, connections):
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * n
    disc = [0] * n
    low = [0] * n
    parent = [-1] * n
    result = []
    time = [0]
    
    def dfs(u):
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    result.append([u, v])
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return result

try:
    n = int(input("ENTER N\n"))
    m = int(input("ENTER NUMBER OF CONNECTIONS\n"))
    connections = []
    print("ENTER CONNECTIONS (u v):")
    for _ in range(m):
        u, v = map(int, input().split())
        connections.append([u, v])
    print(f"CRITICAL CONNECTIONS: {critical_connections(n, connections)}")
except Exception as e:
    print(f"An error occurred: {e}")
