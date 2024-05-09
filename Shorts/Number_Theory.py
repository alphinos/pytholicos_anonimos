

#Algoritmo de Euclides Estendido para Calcular MDC

def MDC(a: int, b: int) -> int:
    if b == 0:
        return a

    return MDC(b, a%b)

print(MDC(152, 56))

