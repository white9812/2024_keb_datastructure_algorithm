## 함수 선언 부분 ##
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


## 전역 변수 선언 부분 ##
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']
#블랙핑크-(레드벨벳-걸스데이,마마무),에이핑크-트와이스-에이핑크 지우려면 지우려고 하는 current에 이젠 블랙핑크랑 트와이스를 연결
## 메인 코드 부분 ##
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:

    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

    memory.append(node)

deleteName = '마마무'

current = root
parent = None
while True:
    if deleteName is current.data:

        if current.left is None and current.right is None:
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
            del current
        #자식이 없을때
        elif current.left is not None and current.right is  None:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
            del current

        elif current.left is None and current.right is not None:
            if parent.left == current:
                parent.left = current.right
            else:
                # print(current.data)
                # print(current.right.data)
                parent.right = current.right #삭제 할 노드(에이핑크 노드)의 오른쪽 링크 노드(트와이스 노드)를 블랙핑크 오른쪽 링크에 연결
            del current

        print(deleteName, '이(가) 삭제됨.')
        break
    elif deleteName < current.data:
        if current.left == None:
            print(deleteName, '이(가) 트리에 없음')
            break
        parent = current
        current = current.left
    else: #양쪽에 자식 노드가 있을때 처리하는 코드가 필요함
        if current.right == None:
            print(deleteName, '이(가) 트리에 없음')
            break
        parent = current
        current = current.right
