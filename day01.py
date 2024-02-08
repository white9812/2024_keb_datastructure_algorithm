
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def print_nodes(start) :
    current = start
    if current is None :
        return
    print(current.data, end = ' ')
    while current.link is not None:
        current = current.link #다음으로 이동하게 해주는 코드
        print(current.data, end = ' ')
    print()
def insert_node(find_data, insert_data) :
    global head, current, pre

    if head.data is find_data :      # 첫 번째 노드 삽입
        node = Node()
        node.data = insert_data
        node.link = head #화사노드의 링크에 다현이 연결됨
        head = node
        return

    current = head #다현부터 시작함
    while current.link is not None :    # 중간 노드 삽입 #지효만 해당이 됨
        pre = current #current의 주소를 pre가 받음
        current = current.link
        if current.data is find_data : #솔라랑 같은지 보는 것
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()                   # 마지막 노드 삽입
    node.data = insert_data #문별 넣고
    current.link = node #끝까지 갔음, 문별의 링크는 none이 되어서 마지막까지 유지됨
def delete_node(delete_data) :
    global head, current, pre

    if head.data is delete_data :         # 첫 번째 노드 삭제
        current = head
        head = head.link
        print(f"{delete_data}이(가)삭제됨")
        del(current)
        return

    current = head                          # 첫 번째  외 노드 삭제
    while current.link is not None :
        pre = current
        current = current.link
        if current.data == delete_data :
            pre.link = current.link
            print(f"{delete_data}이(가)삭제됨")
            del(current)
            return
    print(f"{delete_data}이(가)삭제 할 수 없음")

head, current, pre = None, None, None
data_array = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

    node = Node()		# 첫 번째 노드
    node.data = data_array[0]
    head = node


    for data in data_array[1:] :	# 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node


    print_nodes(head) #이름들만 꺼내서 출력하도록 함
    delete_node("다현")
    print_nodes(head)
    delete_node("재남")
    print_nodes(head)
    insert_node("다현", "화사")
    print_nodes(head)
    insert_node("사나", "솔라")
    print_nodes(head)
    insert_node("동균", "문별") #동균은 찾을 수 없음 지효까지 갔음 그래서 지효의 링크에
                                                 #문별을 연결해줌
    print_nodes(head)