# Необходимо превратить собранное на семинаре дерево
# поиска в полноценное левостороннее красно-черное дерево. 
# И реализовать в нем метод добавления новых элементов с балансировкой.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = "black"

    def insert(self, new_data):
        if self.data > new_data:
            if self.left is None:
                self.left = Node(new_data)
                self.left.color = "red"
            else:
                self.left.insert(new_data)
        elif self.data < new_data:
            if self.right is None:
                self.right = Node(new_data)
                self.right.color = "red"
            else:
                self.right.insert(new_data)

class Black_Red_Three:
    def addNode(self, root, new_data):
        if root is None:
            root = Node(new_data)
            # root.color = "black"
            return root
        if root.data > new_data:
            if root.left is None:
                self.left = Node(new_data)
                self.left.color = "red"
            else: 
                self.left.insert(new_data)
        elif self.data < new_data:
            if self.right is None:
                self.right = Node(new_data)
                self.right.color = "red"
            else:
                self.right.insert(new_data)
            