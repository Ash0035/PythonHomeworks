class AVLNode:
    def __init__(self, word):
        self.word = word              
        self.count = 1               
        self.height = 1               
        self.left = None              
        self.right = None             
class AVLTree:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        return node.height if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left


        y.left = x
        x.right = T2

        self._update_height(x)
        self._update_height(y)

        return y

    def insert(self, word):
        self.root = self._insert(self.root, word)

    def _insert(self, node, word):

        if not node:
            return AVLNode(word)
        if word < node.word:
            node.left = self._insert(node.left, word)
        elif word > node.word:
            node.right = self._insert(node.right, word)
        else:
            node.count += 1  
            return node

        self._update_height(node)

        balance = self._get_balance(node)

        if balance > 1 and word < node.left.word:
            return self._rotate_right(node)

        if balance < -1 and word > node.right.word:
            return self._rotate_left(node)

        if balance > 1 and word > node.left.word:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and word < node.right.word:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if not node:
            return
        self._inorder(node.left, result)
        result.append((node.word, node.count))
        self._inorder(node.right, result)
        
tree = AVLTree()
text = input().split()

for word in text:
    tree.insert(word)

for word, count in tree.inorder():
    print(f"{word}: {count}")
