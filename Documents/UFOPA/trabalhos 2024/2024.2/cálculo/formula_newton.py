import sympy as sp
from time import sleep


def validar_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


def formula_newton(f, f_deriv, x0, tol=1e-6, max_iter=200):
    contar_inter = 0
    for _ in range(max_iter):
        contar_inter += 1
        print(f'Iteração {contar_inter}: x = {x0:.5f}', flush=True)
        sleep(0.02)
        fx_n = f(x0)
        fpx_n = f_deriv(x0)
        if abs(fx_n) < tol:
            return x0, contar_inter
        if fpx_n == 0:
            raise ValueError('Derivada zero. [ERRO]')
        x0 = x0 - fx_n / fpx_n
    raise ValueError('máximo de interações atingido')


def resultado(chute):
    raizes_encontradas = list()
    print(f'A derivada dessa função é {derivada}')
    r_p, iter_p = formula_newton(funcao, funcao_deriv, x0=chute)
    r_n, iter_n = formula_newton(funcao, funcao_deriv, x0=-chute)
    raizp = sp.sympify(r_p)
    raizn = sp.sympify(r_n)
    if f'{raizp:.5f}' == f'{raizn:.5f}':
        print(f'A raiz encontrada foi {raizp:.5f}  (Encontrada em {iter_p} iterações)')
        raizes_encontradas.append(raizp)
    else:
        print(f'As raizes encontradas foram: {raizp:.5f} ({iter_p} iterações) e {raizn:.5f} ({iter_n} iterações)')
        if raizn not in raizes_encontradas:
            raizes_encontradas.append(round(raizn, 5))
        if raizp not in raizes_encontradas:
            raizes_encontradas.append(round(raizp, 5))
        return raizes_encontradas


def menu():
    while True:
        print('------------------------------')
        print('''MENU\n[1] Digitar uma nova função\n[2] Continuar com a mesma função\n[3] Resultados\n[4] Sair''')
        print('------------------------------')
        resposta = str(input(': '))
        if resposta == '1':
            print('ok')
            resultados_geral.clear()
            break
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


def dados_lista(lista):
    if lista is None:
        print("Erro: a lista recebida é None.")
        return  

    if not lista or not isinstance(lista, list) or not isinstance(lista[0], list) or len(lista[0]) < 2:
        return  

    if lista[0][0] not in resultados_geral:
        resultados_geral.append(lista[0][0])
    if lista[0][1] not in resultados_geral:
        resultados_geral.append(lista[0][1])

    for raiz, _ in lista: 
        if raiz not in resultados_geral:
         resultados_geral.append(raiz)


def todas_raizes(lista):
    cont = 0
    while True:
        print('------------------------------')
        print('[1] Raízes positivas\n[2] Raízes negativas\n[3] Todas as raízes')
        print('------------------------------')
        r = str(input(': ')).strip()[0]
        if r == '1':
            print('---------------------')
            for c in range(0, len(lista)):
                if lista[c] > 0:
                    cont += 1
                    print(f'{cont + 1} _ {lista[c]:.5f}')
            print('---------------------')
            sleep(2)
            break
        elif r == '2':
            print('---------------------')
            for c in range(0, len(lista)):
                if lista[c] < 0:
                    cont += 1
                    print(f'{cont + 1} _ {lista[c]:.5f}')
            print('---------------------')
            sleep(2)
            break
        elif r == '3':
            print('---------------------')
            for c in range(0, len(lista)):
                print(f'{c + 1} _ {lista[c]:.5f}')
            print('---------------------')
            sleep(2)
            break
        else:
            print('Digite uma resposta válida....')
            sleep(0.5)


def programa():
    global derivada
    global funcao
    global funcao_deriv
    while True:
        r_temp = list()
        formula_tratada = sp.sympify(formula_digitada)
        derivada = sp.diff(formula_tratada)
        funcao = sp.lambdify(x, formula_tratada)
        funcao_deriv = sp.lambdify(x, derivada)
        print('[M] para ir ao menu')
        while True:
            chute = str(input('Digite um chute: ')).upper().strip()
            if chute == 'M':
                break
            elif validar_numero(chute):
                break
            else:
                print('digite um valor válido')
        if chute == 'M':
            menu()
            break
        r_temp.append(resultado(float(chute)))
        dados_lista(r_temp)


resultados_geral = list()
while True:
    x = sp.symbols('x')
    formula_digitada = str(input('Digite uma função: '))
    programa()
    