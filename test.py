import random
from tree import BinarySearchTree

random.seed(77)

def random_tree(size=42):
    values = random.sample(range(1, 1000), 42)
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def example_tree():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def extended_tree():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def insert_tree():
    values = [10,30,15,5,49,52,35]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree



bst = insert_tree()
bst.levelorder_traversal()
remove0 = [10,5,52]
insert0 = [100,80,70]
remove1 = [15, 49]
values = [10,30,15,5,49,52,35]

  #  tree = BinarySearchTree()

#    for v in values:
 #       tree.insert(v)
 #   tree.inorder_traversal()
  #  print('\n-----')
   # for r in remove0:
#        tree.remove(r)
 #   tree.inorder_traversal()
#    print('\n-----')
#    for v in insert0:
#        tree.insert(v)
#    tree.inorder_traversal()
#    print('\n-----')

#    for r in remove1:
#        tree.remove(r)
#    tree.inorder_traversal()
#    return tree
#bst = extended_tree()
#bst.inorder_traversal()
#bst = random_tree()
#bst = insert_tree()
#bst = exercicios()
print('\n')


# testar remoção da árvore
#print('\n----')
#v = 61
#bst.remove(v)
#print("Após remover {}".format(v))
#bst.inorder_traversal()
#bst.postorder_traversal()
print('\n-----')

#v = 61
#bst.remove(v)
#bst.inorder_traversal()
#bst.postorder_traversal()

#bst.levelorder_traversal()

#print("\n-------")
#print("Máximo:", bst.max())
#print("Mínimo:", bst.min())
#
 #print('\n-----')
#items = [1, 3, 981, 510, 1000]
#for item in items:
#    r = bst.search(item)
#    if r is None:
#        print(item, "não encontrado")
#    else:
#        print(r.root.data, 'encontrado')