from functools import lru_cache
import timeit
import matplotlib.pyplot as plt

@lru_cache(maxsize=None) 
def fibonacci_lru(n):
    if n <= 1:
        return n
    return fibonacci_lru(n-1) + fibonacci_lru(n-2)

class SplayTreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        return left_child

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        return right_child

    def splay(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            if node.left is None:
                return node
            if key < node.left.key:
                node.left.left = self.splay(node.left.left, key)
                node = self.rotate_right(node)
            elif key > node.left.key:
                node.left.right = self.splay(node.left.right, key)
                if node.left.right:
                    node.left = self.rotate_left(node.left)
            return node if node.left is None else self.rotate_right(node)

        else:
            if node.right is None:
                return node
            if key > node.right.key:
                node.right.right = self.splay(node.right.right, key)
                node = self.rotate_left(node)
            elif key < node.right.key:
                node.right.left = self.splay(node.right.left, key)
                if node.right.left:
                    node.right = self.rotate_right(node.right)
            return node if node.right is None else self.rotate_left(node)

    def insert(self, key, value):
        if self.root is None:
            self.root = SplayTreeNode(key, value)
            return
        self.root = self.splay(self.root, key)
        if self.root.key == key:
            return
        new_node = SplayTreeNode(key, value)
        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        self.root = new_node

    def find(self, key):
        self.root = self.splay(self.root, key)
        if self.root is None or self.root.key != key:
            return None
        return self.root.value

def fibonacci_splay(n, tree):
    result = tree.find(n)
    if result is not None:
        return result
    if n <= 1:
        value = n
    else:
        value = fibonacci_splay(n-1, tree) + fibonacci_splay(n-2, tree)
    tree.insert(n, value) 
    return value

n_values = list(range(0, 1001, 50))

lru_times = []
for n in n_values:
    lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=10)
    lru_times.append(lru_time)

tree = SplayTree()
splay_times = []
for n in n_values:
    splay_time = timeit.timeit(lambda: fibonacci_splay(n, tree), number=10)
    splay_times.append(splay_time)

plt.plot(n_values, lru_times, label="LRU Cache")
plt.plot(n_values, splay_times, label="Splay Tree")
plt.xlabel('n')
plt.ylabel('Execution Time (seconds)')
plt.title('Fibonacci Calculation Time Comparison')
plt.legend()
plt.show()

print(f"{'n':<10}{'LRU Cache Time (s)':<25}{'Splay Tree Time (s)'}")
print("-" * 50)
for n, lru, splay in zip(n_values, lru_times, splay_times):
    print(f"{n:<10}{lru:<25}{splay}")
