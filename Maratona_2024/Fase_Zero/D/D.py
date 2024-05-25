E, V = map(int, input().split())

def ajeita_horario(valor: int) -> str:
    if valor < 10:
        return '0'+str(valor)
    else:
        return str(valor)

horas = (19+(E//V))%24

distancia_restante = E%V

minutos = (60*distancia_restante)//V

print(ajeita_horario(horas)+':'+ajeita_horario(minutos))
