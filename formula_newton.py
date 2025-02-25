import sympy as sp
import streamlit as st


def validar_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def formula_newton(f, f_deriv, x0, tol=1e-6, max_iter=200):
    contar_inter = 0
    iteracoes = []
    for _ in range(max_iter):
        contar_inter += 1
        fx_n = f(x0)
        fpx_n = f_deriv(x0)
        iteracoes.append(f"Iteração {contar_inter}: x = {x0:.5f}")
        if abs(fx_n) < tol:
            return x0, contar_inter, iteracoes
        if fpx_n == 0:
            raise ValueError('Derivada zero. [ERRO]')
        x0 = x0 - fx_n / fpx_n
    raise ValueError('Máximo de iterações atingido')

def resultado(chute):
    raizes_encontradas = []
    iteracoes_totais = []
    r_p, iter_p, iteracoes_p = formula_newton(funcao, funcao_deriv, x0=chute)
    r_n, iter_n, iteracoes_n = formula_newton(funcao, funcao_deriv, x0=-chute)
    iteracoes_totais.extend(iteracoes_p + iteracoes_n)
    raizp = sp.sympify(r_p)
    raizn = sp.sympify(r_n)
    if f'{raizp:.5f}' == f'{raizn:.5f}':
        raizes_encontradas.append(raizp)
    else:
        raizes_encontradas.extend([round(raizn, 5), round(raizp, 5)])
    return raizes_encontradas, iteracoes_totais

# Interface principal
def main():
    st.set_page_config(page_title="Método de Newton-Raphson", layout="centered")

    if "formula_digitada" not in st.session_state:
        st.session_state["formula_digitada"] = ""

    # Estilização CSS
    st.markdown(
        """
        <style>
            body { background-color: #0D1B2A; color: #E0E1DD; }
            .stTextInput>div>div>input { background-color: #1B263B; color: #E0E1DD; border-radius: 10px; }
            .stButton>button { 
                background: linear-gradient(to right, #5F0A87, #A4508B);
                color: white; 
                border-radius: 10px;
                width: 100%; 
                font-size: 16px;
                font-weight: bold;
            }
            .stButton>button:hover { background: linear-gradient(to right, #A4508B, #5F0A87); }
        </style>
        """, unsafe_allow_html=True
    )

    st.title('🔎 Encontrar Raízes de Funções')

    # Layout das colunas para inputs e botões
    col1, col2 = st.columns([3, 2])

    with col1:
        formula_digitada = st.text_input('Digite uma função:', value=st.session_state["formula_digitada"])
        chute = st.text_input('Digite um chute inicial:')

    with col2:
        st.write("#### 📌 Exemplos Rápidos")
        if st.button('Teste Inicial:  f(x) = x² - 4'):
            st.session_state["formula_digitada"] = 'x**2 - 4'
            st.rerun()
        if st.button('Desafio 1:  f(x) = x² - 2x'):
            st.session_state["formula_digitada"] = 'x**2 - 2*x'
            st.rerun()
        if st.button('Desafio 2:  f(x) = tan(x) - 1/x'):
            st.session_state["formula_digitada"] = 'tan(x) - 1/x'
            st.rerun()

    if formula_digitada:
        x = sp.symbols('x')
        formula_tratada = sp.sympify(formula_digitada)
        derivada = sp.diff(formula_tratada)
        global funcao, funcao_deriv
        funcao = sp.lambdify(x, formula_tratada)
        funcao_deriv = sp.lambdify(x, derivada)

        if st.button('💡 Calcular Raízes'):
            if validar_numero(chute):
                resultados, iteracoes = resultado(float(chute))

                # Criamos duas colunas para exibir os resultados lado a lado
                col_raizes, col_iteracoes = st.columns([1, 2])

                with col_raizes:
                    st.subheader("✅ Raízes Encontradas:")
                    for raiz in resultados:
                        st.write(f"📌 {raiz}")

                with col_iteracoes:
                    st.subheader("🔄 Iterações:")
                    for iteracao in iteracoes:
                        st.write(iteracao)

            else:
                st.warning('⚠️ Digite um valor numérico válido para o chute inicial.')

if __name__ == '__main__':
    main()
