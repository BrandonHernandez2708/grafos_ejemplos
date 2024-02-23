#escriba un programa de python para crear un arbol de busqueda binaria utilizando elementos de una matriz (dados)
# donde los elementos de una matriz se orden en orden acendene
class nodosarbol(object):
      def __init__(self,x):
        self.val =x
        self.izquierda = None
        self.derecha = None
def ordenamiento_de_arrays_a_bst(nums):
    if not nums:
        return None
    mid_val = len(nums) // 2
    node = nodosarbol(nums[mid_val])
    node.izquierda = ordenamiento_de_arrays_a_bst(nums[:mid_val])
    node.derecha = ordenamiento_de_arrays_a_bst(nums[mid_val+1:])  # Corregir esta línea
    return node

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.izquierda)
    preOrder(node.derecha)

result = ordenamiento_de_arrays_a_bst([1,2,3,4,5,6,7])
preOrder(result)
