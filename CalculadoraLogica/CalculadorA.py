import tkinter as tk
from tkinter import messagebox
from itertools import product

def implica(a, b):
    return (not a) or b

def equivale(a, b):
    return a == b

def xor(a, b):
    return a != b

def verificar_fbf(expr):

    expr = expr.replace(" ", "")

    if expr == "":
        return False

    if "()" in expr or "(¬)" in expr:
        return False

    variaveis = set("pqrst")
    conectivos = set("∧∨→↔⊻")

    for i in range(len(expr) - 2):
        if expr[i] == "(" and expr[i+1] == "¬" and expr[i+2] in conectivos:
            return False

    for i in range(len(expr) - 1):
        if expr[i] == "(":
            j = i + 1
            while j < len(expr) and expr[j] == "¬":
                j += 1
            if j < len(expr) and expr[j] == ")":
                return False

    for c in expr:
        if c not in variaveis and c not in conectivos and c not in "()¬":
            return False

    pilha = []
    for c in expr:
        if c == "(":
            pilha.append(c)
        elif c == ")":
            if not pilha:
                return False
            pilha.pop()

    if pilha:
        return False

    if expr[0] in conectivos or expr[0] == ")":
        return False

    if expr[-1] in conectivos or expr[-1] == "¬" or expr[-1] == "(":
        return False

    for i in range(len(expr)-1):

        a = expr[i]
        b = expr[i+1]

        if a in variaveis and b in variaveis:
            return False

        if a in variaveis and b == "(":
            return False

        if a == ")" and b in variaveis:
            return False

        if a in conectivos and b in conectivos:
            return False

        if a == "(" and b in conectivos:
            return False

        if a in conectivos and b == ")":
            return False

        if a == ")" and b == "(":
            return False

        if a in variaveis and b == "¬":
            return False

        if a == ")" and b == "¬":
            return False

        if a == "¬" and b in conectivos:
            return False

        if a == "¬" and b == ")":
            return False

    return True


def avaliar(expr, valores):
    expr = expr.replace(" ", "")
    return avaliar_rec(expr, valores)


def avaliar_rec(expr, valores):

    while expr.startswith("(") and expr.endswith(")"):
        par = 0
        for i, c in enumerate(expr):
            if c == "(":
                par += 1
            elif c == ")":
                par -= 1
            if par == 0 and i < len(expr) - 1:
                break
        else:
            expr = expr[1:-1]
            continue
        break

    par = 0
    for i in reversed(range(len(expr))):
        c = expr[i]

        if c == ")":
            par += 1
        elif c == "(":
            par -= 1
        elif c == "↔" and par == 0:
            return equivale(
                avaliar_rec(expr[:i], valores),
                avaliar_rec(expr[i+1:], valores)
            )

    par = 0
    for i in reversed(range(len(expr))):
        c = expr[i]

        if c == ")":
            par += 1
        elif c == "(":
            par -= 1
        elif c == "→" and par == 0:
            return implica(
                avaliar_rec(expr[:i], valores),
                avaliar_rec(expr[i+1:], valores)
            )

    par = 0
    for i in reversed(range(len(expr))):
        c = expr[i]

        if c == ")":
            par += 1
        elif c == "(":
            par -= 1
        elif c == "⊻" and par == 0:
            return xor(
                avaliar_rec(expr[:i], valores),
                avaliar_rec(expr[i+1:], valores)
            )

    par = 0
    for i in reversed(range(len(expr))):
        c = expr[i]

        if c == ")":
            par += 1
        elif c == "(":
            par -= 1
        elif c == "∨" and par == 0:
            return (
                avaliar_rec(expr[:i], valores) or
                avaliar_rec(expr[i+1:], valores)
            )

    par = 0
    for i in reversed(range(len(expr))):
        c = expr[i]

        if c == ")":
            par += 1
        elif c == "(":
            par -= 1
        elif c == "∧" and par == 0:
            return (
                avaliar_rec(expr[:i], valores) and
                avaliar_rec(expr[i+1:], valores)
            )

    if expr.startswith("¬"):
        return not avaliar_rec(expr[1:], valores)

    if expr in valores:
        return valores[expr]

    raise ValueError("Expressão inválida")


def adicionar_simbolo(simbolo):
    entrada_var.set(entrada_var.get() + simbolo)


def apagar_ultimo():
    entrada_var.set(entrada_var.get()[:-1])


def limpar_display():
    entrada_var.set("")
    area_tabela.delete("1.0", tk.END)


def mostrar_tabela():

    expressao = entrada_var.get()

    if not verificar_fbf(expressao):
        messagebox.showerror(
            "Erro sintático",
            "A FÓRMULA DIGITADA NÃO SEGUE O PADRÃO FBF"
        )
        return

    variaveis = sorted([v for v in "pqrst" if v in expressao])

    if not variaveis:
        return

    area_tabela.delete("1.0", tk.END)

    cabecalho = " | ".join(variaveis + ["Resultado"]) + "\n"
    area_tabela.insert(tk.END, cabecalho)
    area_tabela.insert(tk.END, "-" * len(cabecalho) + "\n")

    resultados = []

    for combinacao in product([False, True], repeat=len(variaveis)):

        valores = dict(zip(variaveis, combinacao))

        resultado = avaliar(expressao, valores)

        resultados.append(resultado)

        linha = " | ".join(
            ["V" if valores[v] else "F" for v in variaveis] +
            ["V" if resultado else "F"]
        )

        area_tabela.insert(tk.END, linha + "\n")

    area_tabela.insert(tk.END, "\n")

    if all(resultados):
        area_tabela.insert(tk.END, "É UMA TAUTOLOGIA\n")

    elif not any(resultados):
        area_tabela.insert(tk.END, "É UMA CONTRADIÇÃO\n")

    else:
        area_tabela.insert(tk.END, "É UMA CONTINGÊNCIA\n")


janela = tk.Tk()
janela.title("Calculadora Lógica Proposicional")

entrada_var = tk.StringVar()

entrada = tk.Entry(
    janela,
    textvariable=entrada_var,
    width=80,
    font=("Arial", 14)
)

entrada.grid(row=0, column=0, columnspan=6, padx=10, pady=10)


botoes = [

    ("p",0,0),("q",0,1),("r",0,2),
    ("s",0,3),("t",0,4),("¬",0,5),

    ("∧",1,0),("∨",1,1),("⊻",1,2),
    ("→",1,3),("↔",1,4),("(",1,5),

    (")",2,0)

]


for texto,linha,coluna in botoes:

    tk.Button(
        janela,
        text=texto,
        width=6,
        height=2,
        command=lambda t=texto: adicionar_simbolo(t)
    ).grid(row=linha+1,column=coluna,padx=3,pady=3)


tk.Button(
    janela,
    text="DEL",
    width=10,
    height=2,
    command=apagar_ultimo
).grid(row=4, column=4, padx=3, pady=3)


tk.Button(
    janela,
    text="C",
    width=10,
    height=2,
    command=limpar_display
).grid(row=4, column=5, padx=3, pady=3)


tk.Button(
    janela,
    text="Resultado",
    width=40,
    height=2,
    command=mostrar_tabela
).grid(row=5,column=0,columnspan=6,padx=10,pady=5)


quadro = tk.Frame(janela)
quadro.grid(row=6,column=0,columnspan=6)

scroll = tk.Scrollbar(quadro)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

area_tabela = tk.Text(
    quadro,
    width=60,
    height=60,
    yscrollcommand=scroll.set
)

area_tabela.pack()

scroll.config(command=area_tabela.yview)

janela.mainloop()