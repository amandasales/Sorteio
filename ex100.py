from random import randint


def sorteia(lst):
    for c in range(0, 5):
        lst.append(randint(1, 10))
    print(f'foram sorteados 5 valores para a  lista: {lst}')


def somapar(lst):
    soma = 0
    for v in lst:
        if v % 2 == 0:
            soma += v
    print(f'Somados os valores pares da lista, temos {soma}')


lst = []
sorteia(lst)
somapar(lst)
