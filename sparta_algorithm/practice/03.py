class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        # 루트노드를 맨 마지막 노드(맨 아래 레벨의 맨 오른쪽 노드)와 교환
        # (루트노드가 1인 이유: 맨 처음은 None이기 때문)
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        # [None, 4, 7, 6, 2, 5, 8]
        # 노드를 제거하는 함수: pop()
        prev_max = self.items.pop()
        # [None, 4, 7, 6, 2, 5]
        # 루트자리에 있는 4가 7이나 6보다 작기 때문에 아직 맥스힙의 특성을 유지하지 않음
        #   => 4를 끌어내려야 함
        cur_index = 1
        # 현재 인덱스가 맨 끝에 도달할 때까지 반복
        # 왼쪽자식과 오른쪽자식이 배열의 길이보다 길다 = 자식이 없다 (??)
        #   => 이때 반복을 멈춤
        # 현재 인덱스의 자식노드가 self.items의 길이보다 작거나 같을 때까지 반복
        # (왼쪽 자식이 self.items의 인덱스보다 넘어가면 끝남 = 더이상 자식이 나올 수 없음)
        while cur_index <= len(self.items) - 1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            # 부모와 두 자식노드 중 제일 큰 노드 구하기
            # 처음에는 부모가 제일 크다고 가정하고 시작
            max_index = cur_index
            # 왼쪽 자식인덱스와 먼저 비교
            # 왼쪽자식이 존재하는 상황인지 먼저 확인
            #   (= 왼쪽자식 인덱스가 len(self.items -1)보다 작거나 같은지)
            # and 부모노드와 비교해서 더 큰지
            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
            # 두 조건을 모두 만족하면 왼쪽노드가 max_index가 됨
                max_index = left_child_index
            # 오른쪽 노드도 똑같이 비교
            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index
                # 애초에 부모노드가 제일 큰 인덱스라면
            if max_index == cur_index:
                # 더이상 비교가 필요없음 (반복문 중단)
                break
            # 비교가 끝나면 노드의 자리 교환 후
            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            # cur_index를 max_index로 업데이트
            cur_index = max_index
        return prev_max  # 8 을 반환해야 합니다.

max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]





max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]
