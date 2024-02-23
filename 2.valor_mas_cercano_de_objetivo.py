class NodoArboles(object):
    def __init__(self, x):
        self.val = x
        self.izquierda = None
        self.derecha = None

def valor_mas_cercano(root, target):
    if not root:
        return float('inf')
    
    a = root.val
    kid = root.izquierda if target < a else root.derecha
    
    if not kid:
        return a
    
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

result = valor_mas_cercano(root, 19)
print(result)
