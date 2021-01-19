class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(len(all_students)):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)


all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    # 구현해보세요!
    student_dict = LinkedDict()
    no_present_students = []

    for k in present_array:
        student_dict.put(k, k)

    for k in all_array:
        if student_dict.get(k) is None:
            no_present_students.append(k)

    return no_present_students


print(get_absent_student(all_students, present_students))