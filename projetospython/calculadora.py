import tkinter as tk

def clicar_botao(valor):
    texto_atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, texto_atual + str(valor))

def limpar_tela():
    entrada.delete(0, tk.END)

def calcular():
    try:
        expressao = entrada.get()
        expressao = expressao.replace('x', '*')
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("320x450")
janela.configure(bg="#202020")

entrada = tk.Entry(janela, font=("Arial", 24), bg="#202020", fg="#FFFFFF", bd=0, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

for i in range(6):
    janela.rowconfigure(i, weight=1)
for j in range(4):
    janela.columnconfigure(j, weight=1)

botoes = [
    ('C', 1, 0), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('x', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0), ('.', 5, 2), ('=', 5, 3)
]

estilo_numero = {"bg": "#333333", "fg": "#FFFFFF", "font": ("Arial", 16), "bd": 0}
estilo_operador = {"bg": "#F39C12", "fg": "#FFFFFF", "font": ("Arial", 16), "bd": 0}
estilo_limpar = {"bg": "#A9A9A9", "fg": "#000000", "font": ("Arial", 16), "bd": 0}

for (texto, linha, coluna) in botoes:
    if texto == 'C':
        estilo = estilo_limpar
        comando = limpar_tela
    elif texto == '=':
        estilo = estilo_operador
        comando = calcular
    elif texto in ['/', 'x', '-', '+']:
        estilo = estilo_operador
        comando = lambda v=texto: clicar_botao(v)
    else:
        estilo = estilo_numero
        comando = lambda v=texto: clicar_botao(v)
        
    if texto == '0':
        botao = tk.Button(janela, text=texto, command=comando, **estilo)
        botao.grid(row=linha, column=coluna, columnspan=2, padx=2, pady=2, sticky="nsew")
    else:
        botao = tk.Button(janela, text=texto, command=comando, **estilo)
        botao.grid(row=linha, column=coluna, padx=2, pady=2, sticky="nsew")

janela.mainloop()
