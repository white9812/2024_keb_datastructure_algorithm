class Graph() :
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g) :
    print(' ', end = ' ')
    for v in range(g.SIZE) :
        print(nameAry[v], end = ' ')
    print()
    for row in range(g.SIZE) :
        print(nameAry[row], end = ' ')
        for col in range(g.SIZE) :
            print(g.graph[row][col], end= '  ')
        print()
    print()


## 전역 변수 선언 부분 ##
G1 = None
nameAry = ['문별', '솔라', '휘인', '쯔위', '선미', '화사']
mb, sl, hi, zi, sm, hs = 0, 1, 2, 3, 4, 5


## 메인 코드 부분 ##
gSize = 6
G1 = Graph(gSize)
G1.graph[mb][sl] = 1; G1.graph[mb][hi] = 1
G1.graph[sl][mb] = 1; G1.graph[sl][zi] = 1
G1.graph[hi][mb] = 1; G1.graph[hi][zi] = 1
G1.graph[zi][sl] = 1; G1.graph[zi][hi] = 1; G1.graph[zi][sm] = 1; G1.graph[zi][hs] = 1
G1.graph[sm][zi] = 1; G1.graph[sm][hs] = 1
G1.graph[hs][zi] = 1; G1.graph[hs][sm] = 1

print('## G1 무방향 그래프 ##')
printGraph(G1)
