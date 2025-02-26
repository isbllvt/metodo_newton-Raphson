import sympy as sp
from time import sleep


# Validar que uma string é um número
def validar_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

# validar se a função é uma função
def validar_funcao(funcao):
    try:
        sp.sympify(funcao)
        return True
    except ValueError:
        return False


# Fórmula de newton - raphson
def formula_newton(f, f_deriv, x0, tol=1e-6, max_iter=200):
    # interações
    global cont_iter
    cont_iter = 0
    # repete a fórmula até chegar no limite de interações ou alcançar a tolerancia
    for _ in range(max_iter):
        # escreve as interações no console em tempo real
        print(f'{_ + 1} _ {x0:.5f}', flush=True)
        # Contador de interações
        cont_iter += 1
        sleep(0.02)
        fx_n = f(x0)
        fpx_n = f_deriv(x0)
        # definir a tolerância 
        if abs(fx_n) < tol:
            return x0
        # caso a derivada seja zero pare tudo com um erro
        if fpx_n == 0:
            print('[ERRO] Derivada não pode ser igual a zero')
            sleep(2)
            inicio()
        # fórmula
        x0 = x0 - fx_n / fpx_n
    print('[ERRO] Máximo de interações atingido')
    sleep(0.5)
    menu()

# adicionar e salvar os resultados em uma lista
def resultado(chute):
    raizes_encontradas = list()
    print(f'A derivada dessa função é {derivada}')
    print('positivo:')
    print('---------------------')
    r_p = formula_newton(funcao, funcao_deriv, x0=chute)
    print('---------------------')
    iter_p = cont_iter
    print('negativo: ')
    print('---------------------')
    r_n = formula_newton(funcao, funcao_deriv, x0=-chute)
    print('---------------------')
    iter_n = cont_iter
    # transformar as raízes em números
    raizp = sp.sympify(r_p)
    raizn = sp.sympify(r_n)
    # caso as raizes positivas e negativas sejam iguais, apenas uma raíz é encontrada
    if f'{raizp:.5f}' == f'{raizn:.5f}':
        print(f'A raiz encontrada foi {raizp:.5f}')
        raizes_encontradas.append(round(raizp, 5))
        print(f'{cont_iter} iterações')
    # caso contrário as duas raízes são salvas
    else:
        print(f'As raizes encontradas foram: {raizp:.5f} e {raizn:.5f}')
        if raizn not in raizes_encontradas:
            raizes_encontradas.append(round(raizn, 5))
        if raizp not in raizes_encontradas:
            raizes_encontradas.append(round(raizp, 5))
        # print da contagem de raízes
        print(f'{iter_p} iterações positivas, {iter_n} iterações negativas')
    return raizes_encontradas

# menu de interações
def menu():
    while True:
        # Opções e input
        print('------------------------------')
        print('''MENU\n[1] Digitar uma nova função\n[2] Continuar com a mesma função\n[3] Resultados\n[4] Sair''')
        print('------------------------------')
        resposta = str(input(': '))
        if resposta == '1':
            resultados_geral.clear()
            inicio()
        elif resposta == '2':
            programa()
        elif resposta == '3': 
            todas_raizes(resultados_geral)
        elif resposta == '4':
            resultados_geral.clear()
            quit()
        else:
            print('Digite uma opção válida...')
            sleep(0.75)

# vê se um resultado não está na lista pra coloca-lo pra não haver repetições
def dados_lista(lista):
    if len(lista[0]) < 2:
        if lista[0][0] not in resultados_geral:
            resultados_geral.append(lista[0][0])
    else:
        if lista[0][0] not in resultados_geral:
            resultados_geral.append(lista[0][0])
        if lista[0][1] not in resultados_geral:
            resultados_geral.append(lista[0][1])



# menu para as opções de raízes e ver os resultados obtidos
def todas_raizes(lista):
    # contador na lista
    cont = 0
    # menu
    while True:
        # print do menu e input
        print('------------------------------')
        print('[1] Raízes positivas\n[2] Raízes negativas\n[3] Todas as raízes\n[4] Voltar')
        print('------------------------------')
        r = str(input(': ')).strip()[0]
        # apenas raízes positivas
        if r == '1':
            cont = 0
            print('---------------------')
            # caso não haja nenhuma raiz na lista, nenhuma raíz foi encontrada
            if len(lista) == 0:
                print('Nenhuma raiz foi encontrada')
            else:
                # print da lista com apenas raízes positivas
                for c in range(0, len(lista)):
                    if lista[c] > 0:
                        cont += 1
                        print(f'{cont} _ {lista[c]:.5f}')
            print('---------------------')
            sleep(2)
        # apenas raízes negativas
        elif r == '2':
            cont = 0
            print('---------------------')
            if len(lista) == 0:
                print('Nenhuma raiz foi encontrada')
            else:
                # print da lista de raízes negativas 
                for c in range(0, len(lista)):
                    if lista[c] < 0:
                        cont += 1
                        print(f'{cont} _ {lista[c]:.5f}')
            print('---------------------')
            sleep(2)
        elif r == '3':
            cont = 0
            print('---------------------')
            if len(lista) == 0:
                print('Nenhuma raiz foi encontrada')
            else:
                for c in range(0, len(lista)):
                    print(f'{c + 1} _ {lista[c]:.5f}')
            print('---------------------')
            sleep(2)
        elif r == '4':
            break
        else:
            print('Digite uma resposta válida....')
            sleep(0.5)


# função do programa para poder a opção [continuar com a mesma função] funcione.
def programa():
    # global de algumas variáveis para tudo funcionar corretamente
    global derivada
    global funcao
    global funcao_deriv
    #chute = x0
    while True:
        r_temp = list()
        # transformação da string função digitada para um número
        formula_tratada = sp.sympify(formula_digitada)
        # derivada da função em uma função sympy
        derivada = sp.diff(formula_tratada)
        # indicar que o x é a variável da função
        funcao = sp.lambdify(x, formula_tratada)
        funcao_deriv = sp.lambdify(x, derivada)
        print('[M] para ir ao menu')
        # input que volta para ele mesmo caso não digite um valor válido
        while True:
            chute = str(input('Digite o x0: ')).upper().strip()
            if chute == 'M':
                break
            elif validar_numero(chute):
                break
            else:
                print('digite um valor válido')
        if chute == 'M':
            menu()
        # adicionar os resultados na lista temporária
        r_temp.append(resultado(float(chute)))
        # enviar a lista temporária para a lista em que não possa haver repetições
        dados_lista(r_temp)


def inicio():
    global x
    global formula_digitada
    global resultados_geral
    resultados_geral = list()
    while True:
        # definir que 'x' é a variável da função
        x = sp.symbols('x')
        formula_digitada = str(input('Digite uma função: '))
        if validar_funcao(formula_digitada):
            programa()
        else:
            print('digite uma função valida')
    

# [main]
inicio()