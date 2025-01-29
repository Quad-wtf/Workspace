
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(node, value):
    if value < node.value:
        if node.left:
            insert(node.left, value)
        else:
            node.left = Node(value)
    elif value > node.value:
        if node.right:
            insert(node.right, value)
        else:
            node.right = Node(value)

def traverse(node, player_pos):
    if node:
        if player_pos <= node.value:
            traverse(node.left)
            print(node.value, end=' ')
            traverse(node.right)

if __name__ == '__main__':
    root = Node(0)
    [insert(root, value) for value in [-15, -8, 6, 12, 20]]
    traverse(root)