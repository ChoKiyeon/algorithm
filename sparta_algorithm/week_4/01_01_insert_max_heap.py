class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 구현해보세요!
        if len(self.items) == 1:
            self.items.append(value)
            return

        self.items.append(value)

        parents_index = len(self.items) // 2
        insert_index = len(self.items) - 1

        while self.items[parents_index] < self.items[insert_index]:
            self.items[parents_index], self.items[insert_index] = self.items[insert_index], self.items[parents_index]
            if parents_index <= 1:
                break

            insert_index = parents_index
            parents_index = insert_index // 2

        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
