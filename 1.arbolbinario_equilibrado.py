#escriba un programa de python para crear un arbol de busqueda binaria utilizando elementos de una matriz (dados)
# donde los elementos de una matriz se orden en orden acendene
class nodosarbol(object):
      def __init__(self,x):
        self.val =x
        self.izquierda = None
        self.derecha = None
def ordenamiento_de_arrays_a_bst(nums): #devuelve la raíz de un árbol binario utilizando la recursividad dividiendo la matriz por la mitad en cada llamada
    #eligiendo el elemento en la mitad como nodo actual.
    if not nums:
        return None
    mid_val = len(nums) // 2 #Llama recursivamente a preOrder para el subárbol izquierdo.
    node = nodosarbol(nums[mid_val])
    node.izquierda = ordenamiento_de_arrays_a_bst(nums[:mid_val])
    node.derecha = ordenamiento_de_arrays_a_bst(nums[mid_val+1:])  # Corregir esta línea
    return node

#imprime el valor del nodo actual antes de visitar sus nodos izquierdo y derecho. 
def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.izquierda) #Llama recursivamente a preOrder para el subárbol izquierdo.
    preOrder(node.derecha) #Llama recursivamente a preOrder para el subárbol derecho 

result = ordenamiento_de_arrays_a_bst([1,2,3,4,5,6,7])
preOrder(result)
