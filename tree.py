ROOT = 'root'
from queue import Queue
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
    #vai pecorrer a arvore de forma simetrica
    def simetric_traversal(self, node=None):
        if node is None: #vai pecorrer a partir da raiz
            node = self.root
        if node.left:
            print("(", end='')
            self.simetric_traversal(node.left)

        print(node, end='')

        if node.right:
            self.simetric_traversal(node.right)
            print(")", end='')

    def inorder_traversal(self, node=None):
        if node is None: #vai pecorrer a partir da raiz
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    # vai pecorrer a arvore em pós ordem
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if node.left:
            self.postorder_traversal(node.left)

        if node.right:
            self.postorder_traversal(node.right)

        print(node, end=" ")

    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root
        queue = Queue()
        queue.push(node)
        plt.scatter([1, 2, 3, 4], [1, 2, 3, 4])
        plt.ylabel('Eixo Y')
        plt.xlabel('Eixo X')
        plt.title('Novo Gráfico')
        plt.xticks([0, 1, 2, 3, 4, 5, 6])
        plt.yticks([0, 2, 4, 6])
        plt.legend()

        while len(queue):
            node = queue.pop()
            #print(node)
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)

            print(node, end=' ')

        plt.show()

    def heigth(self, node=None):
        if node is None:
            node = self.root
        hLeft = 0
        hRight = 0
        if node.left:
            hLeft = self.heigth(node.left)
        if node.right:
            hRight = self.heigth(node.right)

        if hRight > hLeft:
            return hRight + 1 #tamanho da subarvore + 1
        else:
            return hLeft +1

class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data: # se o número do nó for maior que o número que estamos inserindo ele vai ficar na esquerda
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)

    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.right:
            node = node.right
        return node.data

    # REMOVENDO da Árvore Binária de Busca
    def remove(self, value, node=ROOT):
        # Se for o valor padrão, executa a partir da raiz
        if node == ROOT:
           node = self.root
        # Se desceu até um ramo nulo, não há nada a fazer
        if node is None:
            return node
        # Se o valor for menor, desce à esquerda
        if value < node.data:
            node.left = self.remove(value, node.left)
        # Se o valor for maior, desce à direita
        elif value > node.data:
            node.right = self.remove(value, node.right)
        #encontramos o número
        # Se não for nem menor, nem maior, encontramos! Vamos remover...
        else:
            #verificamos se existe elementos após o selecionado
            if node.left is None: #caso com elemento de um lado
                return node.right
            if node.right is None: #caso com elemento de um lado
                return node.left
            else:  #caso com dois filhos
                # Substituto é o sucessor do valor a ser removido
                # sucessor é o maoir número após o que será removido ou seja sempre esta a direita
                substitute = self.min(node.right)
                # Ao invés de trocar a posição dos nós, troca o valor
                node.data = substitute
                # Depois, remove o substituto da subárvore à direita
                node.right = self.remove(substitute, node.right)

        return node

def exemplo_basic():
    tree = BinaryTree(9)
    tree.root.left = Node(1)
    tree.root.right = Node(1)
    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)

def exemplo_simetric():
    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2

    tree.simetric_traversal()
    print("")

    #      '+'
    #    /     \
    #  'a'      '*'
    #          /   \
    #        'b'    '-'
    #              /    \
    #            '/'    'e'
    #           /   \
    #         'c'   'd'

    # (a + (b * ((c/d) - e)))

def exemplo_postorder():
    print("Pós-Ordem")
    tree = BinaryTree()
    n1 = Node('I')
    n2 = Node('N')
    n3 = Node('S')
    n4 = Node('C')
    n5 = Node('R')
    n6 = Node('E')
    n7 = Node('V')
    n8 = Node('A')
    n11 = Node('-')
    n9 = Node('5')
    n0 = Node('3')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n11 # o n11 foi incluido depois
    n11.left = n7
    n11.right = n8


    tree.root = n0
    tree.postorder_traversal()

    print("Altura: ", tree.heigth())



if __name__ == "__main__":
    #exemplo_basic()
    #exemplo_simetric()
    exemplo_postorder()





