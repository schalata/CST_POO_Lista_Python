import sys
from datetime import datetime
from datetime import date
import calendar
from math import pi, pow


# Escreva um programa para calcular o volume de ume esfera, onde v = 4/3 Pi r³. Mostre o volume com 2 casas decimais.
def ex1():
    raio = float(input('Digite o valor do raio: '))
    vol = 4/3*pi*raio**3
    print(f'O volume da esfera de raio {raio} é {vol:.2f}')  
    #vol = 4/3*pi*(pow(raio, 3))
    #print(f'O volume da esfera de raio {raio} é {vol:.2f}')
    

# Escreva um programa que forneça a versão utilizada do Python
def ex2():
    print(f'Versão do Python: {sys.version}')
    print(f'Informações da versão: {sys.version_info}')


# Escreva um programa para mostrar a data e hora atual, no formato dia/mês/ano hora:minuto:segundo
def ex3():
    agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(f'Data e hora atual: {agora}')


# Escreva um programa que receba o primeiro e o último nome e imprima em ordem reversa com um espaço
# entre eles
def ex4():
    primeiro_nome = input('Digite seu primeiro nome: ')
    ultimo_nome = input('Digite seu último nome: ')
    print(f'{ultimo_nome} {primeiro_nome}')
  
# Escreva um programa que receba uma sequência de números separados por vírgula e gere uma lista e uma tupla com eles.
def ex5():
  valores = input('Entre com algumas números separados por vírgula: ')
  lista_str = valores.split(',')
  # O map vai aplicar uma função em cada item de uma lista de itens, ou seja, é um for com uma chamada da função para aplicá-la a cada item da sua lista
  lista_int = list(map(int, lista_str))
  tupla = tuple(lista_int)
  print('Lista: ', lista_int)
  print('Tupla: ', tupla)

# Sobre a função map()
# Temos a criação de uma função bem simples, que vai apenas adicionar um “imposto” de 10% em um preço da lista.

# precos = [1000, 1500, 1250, 2500]

#def adicionar_importo(preco):
#    return preco * 1.1

# https://www.hashtagtreinamentos.com/map-no-python


# Escreva um programa que receba um nome de arquivo (nome e extensão) e imprima sua extensão
def ex6():
    filename = input('Escreva um nome de arquivo: ')
    extensao = filename.split(".")  # Cria uma lista com 2 elementos: o nome e a extensão do arquivo
    print(f'A extensão do arquivo é {extensao[-1]}')


# Escreva um programa que imprime a primeira e a última cor de uma lista de cores
def ex7():
    cores = ['Vermelho', 'Amarelo', 'Rosa', 'Rosa', 'Roxo', 'Azul', 'Verde']
    print(f'Primeira cor: {cores[0]} \nÚltima cor: {cores[-1]}')


# Escreva um programa que leia um valor (n) inteiro e escreva a soma de n + nn + nnn
def ex8():
    # a = int(input('Digite um valor inteiro: '))
    # n1 = a
    # n2 = int(str(a) + str(a))
    # n3 = int(str(a) + str(a) + str(a))
    # print(n1 + n2 + n3)


    a = input('Digite um valor inteiro: ')
    n1 = int(a)
    n2 = int(a + a)
    n3 = int(a + a + a)
    print(n1 + n2 + n3)


# Escreva um programa para imprimir a documentação de uma função do Python.
def ex9():
    print(pow.__doc__)


# Escreva um programa em Python que imprima o calendário de um dado mês e ano
def ex10():
    ano = int(input('Digite um ano: '))
    mes = int(input('Digite um mês: '))
    print(calendar.month(ano, mes))


# Escreva um programa para calcular o número de dias entre duas datas
def ex11():
    # Tratamento da data inicial
    data_inicial = input('Entre com a data inicial (formato: dd/mm/aaaa): ')
    data_inicial = data_inicial.split("/")  # Cria uma lista com 3 elementos: dia, mês e ano
    data_inicial = date(int(data_inicial[2]), int(data_inicial[1]), int(data_inicial[0]))

    # Tratamento da data final
    data_final = input('Entre com a data final (formato: dd/mm/aaaa): ')
    data_final = data_final.split("/")
    data_final = date(int(data_final[2]), int(data_final[1]), int(data_final[0]))

    # Diferença dos dias
    delta = data_final - data_inicial
    print(delta.days)


# Escreva um problema que retorne a diferença entre um dado número e 17. Se o número for maior que 17, retorne o valor
# absoluto do dobro da diferença.
def ex12():
    def diferenca(num):
        if num <= 17:
            return 17 - num
        else:
            return (num - 17) * 2

    n = int(input("Digite um valor: "))
    print(diferenca(n))


# Escreva um programa para testar se um número está 100 unidades próximo de 1000 ou 2000
def ex13():
    def proximo(n):
        return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)

    num = int(input("Digite um valor: "))
    print(proximo(num))


# Escreva um programa que imprima n cópias de uma dada string
def ex14():
    nome = input("Digite uma sequência qq de caracteres: ")
    rep = int(input("Quantas vezes deseja repetir a string?: "))
    print(nome * rep)


# Faça um programa que verifica se uma string começa com "ab". Se começar, escreve a string, senão escreva a string
# com "ab" na frente.
def ex15():
    def new_string(st):
        if len(st) >= 2 and st[:2] == 'ab':
            return st
        return 'ab' + st

    string = input("Digite uma string: ")
    print(new_string(string))


# Escreva um programa para contar quantas vezes um determinado número aparece numa lista.
# Leia a lista de números e o número a ser comparado. Forneça a lista de números, separados por vírgula.
def ex16():

    valores = input('Digite um grupo de valores separados por vírgula: ')
    lista_str = valores.split(',')
    
  
    lista_int = list(map(int, lista_str))

    n = int(input('Digite um número: '))
    print(f'O número {n} aparece na lista de valores {lista_int.count(n)} vezes')


# Escreva um programa que receba um valor n (número inteiro não negativo) e imprima n vezes os 2 primeiros caracteres
# de um string dado. Se o string tiver menos de dois caracteres, imprime o string n vezes.
def ex17():
    def substring_copy(string, n):
        tam = 2
        if tam > len(string):
            tam = len(string)
        substr = string[:tam]

        result = ''
        for i in range(n):
            result = result + substr
        return result

    num = int(input('Digite com um número inteiro não negativo: '))
    nome = input('Digite uma string qualquer ')

    print(substring_copy(nome, num))


# Escreva um programa para testar se uma letra é vogal ou consoante
def ex18():
    def eh_vogal(vogal):
        vogais = 'aeiouAEIOU'
        return vogal in vogais

    letra = input('Digite uma letra: ')

    if eh_vogal(letra):
        print(f'A letra {letra} é vogal.')
    else:
        print(f'A letra {letra} é consoante.')


# Escreva um programa para concatenar todos os elementos de uma lista de strings.
def ex19():
    def concatenar_dados_lista2(lista):
        return ''.join(lista)

    print(concatenar_dados_lista2(['1', '2', '3', '4', '9']))


# Escreva um programa para concatenar todos os elementos de uma lista de inteiros.
def ex20():
    def concatenar_dados_lista(lista):
        result = ''
        for elemento in lista:
            result += str(elemento)
        return result

    print(concatenar_dados_lista([1, 2, 3, 4, 9]))


# Listar maior elemento de uma lista
def ex21():
    lista = [1, 10, 3, 4, 11]
    print(max(lista))


# Segundo maior elemento de uma lista
def ex22():
    lista = [1, 10, 3, 4, 11]
    lista.sort()
    print(lista[-2])


# Para 10 valores digitados, separar os pares dos ímpares, colocando em duas listas diferentes.
# Ao final diga quantos elementos tem cada lista e imprima seus valores.
def ex23():
    par = []
    impar = []
    for i in range(10):
        n = int(input('Digite um valor: '))
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)

    print(f'A lista de valores pares tem {len(par)} e seus elementos são: {par}')
    print(f'A lista de valores ímpares tem {len(impar)} e seus elementos são: {impar}')


# Juntar duas listas (numa terceira), ordenar os valores e dizer seu tamanho
def ex24():
    a = [3, 5, 10]
    b = [11, 7, 8]
    c = a + b
    print(f'A junção das listas A e B é {c}.')
    c.sort()
    print(f'Seus valores ordenados são {c} e seu tamanho é {len(c)}')


# Ordenar uma lista de acordo com o 2o elemento (lista de listas)
#
# def ex25(): # Solução usando lógica de programação
#     a = [['A', 43], ['B', 12], ['C', 23], ['D', 8], ['E', 19]]
#     for i in range(len(a)):
#         for j in range(len(a)-i-1):
#             # print(f'[{i}{j} - {a}]')
#             if a[j][1] > a[j+1][1]:
#                 temp = a[j]
#                 a[j] = a[j+1]
#                 a[j+1] = temp
#     print(a)

#     print(sorted(a))

# Se a[01] > a[11] troca. Maior valor em a[11] - O 2o índice (fixo em 1) é para comparar pelo 2o elemento
# Se a[11] > a[21] troca. Menor valor em a[21]
# Se a[21] > a[31] troca. Menor valor em a[31]
# Se a[31] > a[41] troca. Menor valor em a[41] - Ao final, a última lista da lista a, será a maior

# E repete o processo...
# i = 0; j = 0, j = 1, j = 2, j = 3
# i = 1; j = 0, j = 1, j = 2
# i = 2; j = 0, j = 1
# i = 3; j = 0
# i = 4

# Resultado:
# a = [['D', 8], ['B', 12], ['E', 19], ['C', 23], ['A', 43]]

def ex25():  # Solução usando recursos do Python
  a = [['A', 43], ['B', 12], ['C', 23], ['D', 8], ['E', 19]]

  def pega_segundo_elemento(a):
    return a[1]

  a.sort(key=pega_segundo_elemento)

  print(a)


if __name__ == '__main__':
    
    opcoes = {1: ex1, 2: ex2, 3: ex3, 4: ex4, 5: ex5, 6: ex6, 7: ex7, 8: ex8, 9: ex9, 10: ex10,
              11: ex11, 12: ex12, 13: ex13, 14: ex14, 15: ex15, 16: ex16, 17: ex17, 18: ex18, 19: ex19, 20: ex20,
              21: ex11, 22: ex12, 23: ex13, 24: ex14, 25: ex25}

    while True:
        exemplo = int(input('Digite o exemplo a ser executado: '))
        if exemplo in opcoes:  # Verifica se o valor digitado está no dict opcoes
            opcoes.get(exemplo)()  # A função get() retorna o valor referente a chave, fazendo uma chamada a função.
            break  # Depois de executar a função termina o programa. Se comentada essa linha, fica no loop.
        else:
            print('Valor inválido. Tente novamente!')  # Caso a opção seja inválida.
