# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicador = criar_multiplicador(2)
triplicador = criar_multiplicador(3)
quadruplicador = criar_multiplicador(4)

for numero in (2,3,4,5):
    print('duplicador: ',duplicador(numero), end= '\n', sep= '')
    print('triplicador: ',triplicador(numero), end= '\n', sep= '')
    print('quadruplicador: ',quadruplicador(numero), end= '\n', sep= '')