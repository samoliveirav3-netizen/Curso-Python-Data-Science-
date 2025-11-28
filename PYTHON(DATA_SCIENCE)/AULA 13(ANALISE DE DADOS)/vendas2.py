import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import customtkinter


def ler_dado():
    dados = pd.read_csv('AULA 13(ANALISE DE DADOS)/vendas.csv')
    nome  =  dados['vendedor']
    vendas = dados['vendas']
    
    fig, grafico = plt.subplots()
    grafico.plot(nome, vendas)


    
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


def ler_barra():
    dados = pd.read_csv('AULA 13(ANALISE DE DADOS)/vendas.csv')
    nome  =  dados['vendedor']
    vendas = dados['vendas']
    
    plt.figure(figsize=(6,4))
    fig, grafico = plt.subplots()
    grafico.bar(nome, vendas)
    
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()                                                                #Comando para colocar o grafico dentro da interface grafica
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True) 


def ler_esta():
    dados = pd.read_csv('AULA 13(ANALISE DE DADOS)/vendas.csv')
    nome  =  dados['vendedor']
    vendas = dados['vendas']

    df =  pd.DataFrame(dados)
    estatis  =  df.describe()
    estatistica.config(text=estatis)


root = tk.Tk()
root.geometry('2100x1700')
root.configure(bg = 'black')
root.title('Gerador de graficos')
tk.Label(root,text='GRAFICO DE BARRA', font=('arial',12), bg= 'black', fg = 'white').pack(pady=10)
customtkinter.CTkButton(root, text='gerar grafico linha', font=('arial',12), command=ler_dado).pack(pady=10)
customtkinter.CTkButton(root, text='gerar grafico barra', font=('arial',12), command=ler_barra).pack(pady=10)
customtkinter.CTkButton(root, text='gerar estatistica', font=('arial',12), command=ler_esta).pack(pady=10)

estatistica =  tk.Label(root, text='')
estatistica.pack() 

# button = customtkinter.CTkButton(root, text="my button", command=button_callback)
# button.pack(padx=20, pady=20)

root.mainloop()

