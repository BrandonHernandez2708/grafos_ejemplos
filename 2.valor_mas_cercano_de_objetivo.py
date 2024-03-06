class NodoArboles(object):
    def __init__(self, x):
        self.val = x
        self.izquierda = None
        self.derecha = None

def valor_mas_cercano(root, target):
    #root : es el nodo raíz del árbol , target: el valor para el cual se quiere encontrar el valor más cercano.
    if not root: 
        return float('inf')
    
    a = root.val
    kid = root.izquierda if target < a else root.derecha
    
    if not kid:
        return a
    
    #Se determina cuál es el hijo (kid) al que se debe descender en el árbol. Si target es menor que a, se elige el nodo izquierdo
    #de lo contrario se elige el nodo derecho 
    b = valor_mas_cercano(kid, target)
    return min((a, b), key=lambda x: abs(target - x))

root = NodoArboles(8)
root.izquierda = NodoArboles(5)
root.derecha = NodoArboles(14)
root.izquierda.izquierda = NodoArboles(4)
root.izquierda.derecha = NodoArboles(6)
root.izquierda.derecha.izquierda = NodoArboles(7)
root.derecha.derecha = NodoArboles(24)
root.derecha.derecha.izquierda = NodoArboles(22)

result = valor_mas_cercano(root, 19) # el valor mas cercano a 19 es 22 asi que imprime el numero 22 
print(result)
