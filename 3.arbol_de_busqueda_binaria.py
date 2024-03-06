class NodoArboles(object):
    def __init__(self, x):
        self.val = x
        self.izquierda = None
        self.derecha = None

def is_BST(root): # utiliza un enfoque de recorrido inorden utilizando una pila.
    stack = []
    prev = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.izquierda
        root = stack.pop()
        if prev and root.val <= prev.val:
            return False
        #Si el valor es menor o igual, entonces el árbol no es un BST válido y la función devuelve False.
        # De lo contrario, se actualiza prev y se avanza al nodo derecho.
        prev = root
        root = root.derecha

    return True  
root = NodoArboles(2)
root.izquierda = NodoArboles(1)
root.derecha = NodoArboles(3)

result = is_BST(root) #el árbol es un BST válido
print(result)
root = NodoArboles(1)
root.izquierda = NodoArboles(2)
root.derecha = NodoArboles(3)

result = is_BST(root) #el árbol no es un BST válido, 
print(result)


            