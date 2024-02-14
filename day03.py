
'''
G1=None
nameAry=["문별","솔라","휘인","쯔위","선미","화사"]
mb,sl,hi,zz,sm,hs=0,1,2,3,4,5
'''
#깊이 우선 탐색
def dfs(g,v,visited):
    visited[v]=1
    print(chr(ord("A")+v),end=' ')
    for i in range(len(g)):
        if graph[v][i] ==1 and not visited[i]: #왜 1이 아니라 True? 1일때랑 true 일때랑 다름
            dfs(g,i,visited)
graph=[
    [0,1,1,0,0,0], #문별
    [1,0,0,1,0,0], #솔라
    [1,0,0,1,0,0], #휘인
    [0,1,1,0,1,1], #쯔위
    [0,0,0,1,0,1], #선미
    [0,0,0,1,1,0]  #화사
]

visited=[0 for _ in range(len(graph))]
visited=[0]*len(graph)
dfs(graph,0,visited)

