# Задание 1
class Stack:
    def __init__(self):
        self.array = []

    def push(self, items):
        for item in items:
            self.array.append(item)

    def pop(self, index=-1):
        if index < -1:
            raise IndexError("Мне лень делать негативные индексы")
        temp = 0
        if index == -1 or index >= len(self.array):
            self.array = self.array[0:-1]
        else:
            while temp != index:
                temp += 1
            else:
                self.array = self.array[0:temp] + self.array[temp + 1:]

    def top(self):
        if self.array:
            return self.array[-1]
        else:
            return False

    def empty(self):
        if self.array:
            return False
        else:
            return True

    def main(self):
        if self.empty():
            return "No"
        if self.top() == "(":
            return "No"
        if self.array[0] == ")":
            return "No"

        temp = []
        for item in self.array:
            if item == "(":
                temp.append(item)
            else:
                temp.pop()
        if not temp:
            return "Yes"
        else:
            return "No"

'''
sequence = [x for x in input().strip("")]
stack = Stack()
stack.push(sequence)
print(stack.main())
'''


# Задание 2
class HashTable:
    def __init__(self, size=11):
        self.operations = int(input())
        self.size = size
        self.buckets = [[] for x in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        if self.operations > 0:
            data = (key, value)
            self.buckets[self._hash(data[0])].append(data)
            self.operations -= 1

    def search(self, key):
        pass

    def delete(self, key):
        for i in range(len(self.buckets[self._hash(key)])):
            if self.buckets[self._hash(key)][i][0] == key:
                self.buckets[self._hash(key)].pop()
                break

    def display(self):
        print(self.buckets)


table = HashTable()
table.insert(1, 15)
table.insert(12, 45)
table.insert(13, 155)
table.insert(11, 175)
table.insert(12, 185)
table.delete(12)
table.display()
