class NodoArboles(object):
    def __init__(self, x):
        self.val = x
        self.izquierda = None
        self.derecha = None

def ordenamiento_de_arrays_a_bst(nums):  #devuelve la raíz de un árbol binario utilizando la recursividad dividiendo la matriz por la mitad en cada llamada
    #eligiendo el elemento en la mitad como nodo actual.
    if not nums:
        return None
    mid_val = len(nums) // 2
    node = NodoArboles(nums[mid_val])
    node.izquierda = ordenamiento_de_arrays_a_bst(nums[:mid_val])
    node.derecha = ordenamiento_de_arrays_a_bst(nums[mid_val+1:])
    return node

def preOrder(node): # El recorrido preorden sigue el orden de raíz, izquierda, derecha.
    if not node:
        return
    print(node.val)
    preOrder(node.izquierda)
    preOrder(node.derecha)

arrays_nums = [1, 2, 3, 4, 5, 6, 7]
print("Array original:")
print(arrays_nums) 
result = ordenamiento_de_arrays_a_bst(arrays_nums) #se llama a la funcion 
print("\nArray a árbol balanceado:")
preOrder(result)
