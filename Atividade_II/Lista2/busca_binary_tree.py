class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def _inorder_recursive(self,root, v):
        if root:
            self._inorder_recursive(root.left, v)
            v.append(root.value)
            self._inorder_recursive(root.right, v)
        return v

    def _preorder_recursive(self,root, v):
        if root:
            v.append(root.value)
            self._preorder_recursive(root.left, v)
            self._preorder_recursive(root.right, v)
        return v


    def _postorder_recursive(self, root, v):
        if root:
            self._postorder_recursive(root.left , v)
            self._postorder_recursive(root.right, v)
            v.append(root.value)
        return v

# Testando a árvore binária

test_cases = 1
for _ in range(int(input())):
    tree = BinaryTree()
    n = int(input())
    lista = [int(x) for x in input().split()]
    for i in lista:
        tree.insert(i)
    postorder = tree._postorder_recursive(tree.root, [])
    inorder = tree._inorder_recursive(tree.root, [])
    preorder = tree._preorder_recursive(tree.root, [])
    print(f'Case {test_cases}:')
    test_cases+=1
    print('Pre.: ',end='')
    for i in range(len(preorder)):
        if i != len(preorder) - 1:
            print(preorder[i], end=' ')
        else:
            print(preorder[i])
    print('In..: ',end='')
    for i in range(len(inorder)):
        if i != len(inorder) - 1:
            print(inorder[i], end=' ')
        else:
            print(inorder[i])
    print('Post: ',end='')
    for i in range(len(postorder)):
        if i != len(postorder) - 1:
            print(postorder[i], end=' ')
        else:
            print(postorder[i])
    print()