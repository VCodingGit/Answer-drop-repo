class Node:
    def __init__(self, val=None):
        self.val = val
        self.next_el = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.length = 0

    def add_to_head(self, *vals):
        for val in vals:
            self.length += 1
            node = Node(val)
            node.next_el = self.head
            self.head = node

    def __str__(self):
        line = []
        temp = self.head
        while temp:
            line.append(str(temp.val))
            temp = temp.next_el
        return " -> ".join(line)

    def __len__(self):
        return self.length

    def search(self, *vals):
        temp = []
        elem = self.head
        counter = 0
        found = False
        ans = {}
        while elem:
            temp.append(elem.val)
            elem = elem.next_el
        temp.pop()
        for val in vals:
            ans[val] = ""
            for element in temp:
                if val == element:
                    ans[val] = ans[val] + " " + str(counter)
                    temp.insert(counter, None)
                    del temp[counter + 1]
                    found = True
                counter += 1
            if not found:
                ans[val] = str(-1)
            found = False
            counter = 0
        for val in vals:
            print(f"{[int(x) for x in ans[val].split()]}".replace("[", "").replace("]", ""))

    def add_to_tail(self, val):
        temp = self.head
        storage = []
        while temp:
            storage.append(temp.val)
            temp = temp.next_el
        storage.pop()
        storage.append(val)
        storage = reversed(storage)
        self.length = 0
        self.head = Node()
        LinkedList.add_to_head(self, *storage)

    def insert(self, position, val):
        if position > self.length - 1:
            LinkedList.add_to_tail(self, val)
        if position < 0:
            raise IndexError
        else:
            counter = 0
            temp = self.head
            storage = []
            while temp:
                if counter == position:
                    storage.append(val)
                    storage.append(temp.val)
                else:
                    storage.append(temp.val)
                temp = temp.next_el
                counter += 1
            storage.pop()
            storage = reversed(storage)
            self.length = 0
            self.head = Node()
            LinkedList.add_to_head(self, *storage)

    def delete_element(self, elem):
        temp = self.head
        storage = []
        flag = False
        while temp:
            if temp.val == elem:
                temp = temp.next_el
                flag = True
                break
            else:
                storage.append(temp.val)
                temp = temp.next_el
        while temp:
            storage.append(temp.val)
            temp = temp.next_el
        storage.pop()
        self.length = 0
        self.head = Node()
        storage = reversed(storage)
        LinkedList.add_to_head(self, *storage)
        return flag

    def transform_to_array(self):
        temp = self.head
        storage = []
        while temp:
            storage.append(temp.val)
            temp = temp.next_el
        storage.pop()
        return [x for x in storage]


# Инициализация
l_l_e = LinkedList()
useless_var = input("Random symbol ---> ")
values = [int(x) for x in input("Sequence ---> ").split()]
search_vals = [int(x) for x in input("Searching for ---> ").split()]
l_l_e.add_to_head(*values)

# Задание 1
print("#BLOCK 1#")
print(l_l_e, "\n", len(l_l_e), sep="")
l_l_e.search(*search_vals)

# Задание 2
print("#BLOCK 2#")
print(l_l_e)
l_l_e.insert(*[int(x) for x in input("Position & Value to insert: ").split()])
print(l_l_e.delete_element(int(input("Element to delete: "))))
print(l_l_e)
print(l_l_e.transform_to_array())
