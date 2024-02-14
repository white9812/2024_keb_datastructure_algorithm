## 함수 선언부 예제문제
class Graph:
    def __init__ (self, size) :
        self.SIZE = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size) ]
g=Graph(3)
print(g.graph) # 3x3 matrix

# # 전역 변수부
# G1, G3 = None, None
#
# 메인 코드부
G1 = Graph(4) #4x4
G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[1][3] = 1
G1.graph[2][1] = 1
G1.graph[3][0] = 1
G1.graph[3][1] = 1

print('##  G1 무방향 그래프 ##')
for row in range(G1.SIZE):
    for col in range(G1.SIZE): #4라고 바로 쓰는거 보다는 정수 리터럴을 쓴ㄴ게 좋음
        print(G1.graph[row][col], end=' ')
    print() # 행이 바뀌는 시점에는 줄바꿈하기
