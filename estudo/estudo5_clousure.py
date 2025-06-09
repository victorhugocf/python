# Closure é um conceito da programação onde uma função "lembra" o ambiente em que foi criada, mesmo depois desse ambiente ter sido finalizado.
# Crie fuções que duplicam, triplicam e quadriblicam o numero recebido

def multiplicador(multiplicador):
    def multiplicacao(numero):
        return multiplicador * numero
    return multiplicacao

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

numero = int(input('Digite um número: '))

print(duplicar(numero))
print(triplicar(numero))
print(quadruplicar(numero))