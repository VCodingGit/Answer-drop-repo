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


sequence = [x for x in input().strip("")]
stack = Stack()
stack.push(sequence)
print(stack.main())


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
            buck_adr = self._hash(key)
            if not self.buckets[buck_adr]:
                self.buckets[buck_adr].append(data)
                self.operations -= 1
                return
            if self.buckets[buck_adr][0][0] == key:
                self.buckets[buck_adr].append(data)
                self.operations -= 1
                return
            else:
                for i in range(0, len(self.buckets)):
                    if not self.buckets[i]:
                        self.buckets[i].append(data)
                        self.operations -= 1
                        return
                    elif self.buckets[i][0][0] == key:
                        self.buckets[i].append(data)
                        self.operations -= 1
                        return
                else:
                    self.buckets.append([data])
                    self.size += 1
                    self.operations -= 1
                    return

    def search(self, key, default=0):
        for i in range(0, self.size):
            try:
                if self.buckets[i][0][0] == key:
                    return self.buckets[i][default][1]
            except IndexError:
                pass
        return None

    def delete(self, key):
        flag = False
        for i in range(len(self.buckets[self._hash(key)])):
            if self.buckets[self._hash(key)][i][0] == key:
                self.buckets[self._hash(key)].pop()
                return flag
        else:
            return False

    def display(self):
        print(self.buckets)


table = HashTable()
while table.operations > 0:
    x, y = [int(x) for x in input().split()]
    table.insert(x, y)
x = int(input())
y = int(input())
d = int(input())
print(table.search(x))
print(table.search(y, 1))
print(table.delete(d))
table.display()
