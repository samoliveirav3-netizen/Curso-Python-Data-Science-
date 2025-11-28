import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd


# mais 3 funções bar -  plot -  scarter


def mostra_grafico():
    dados  =  pd.read_csv('DataSete/interface_grafico.csv')
    plt.figure(figsize=(8,6))
    plt.pie(dados['vendas'],labels=dados['mes'], autopct='%1.1f%%')
    plt.title('VENDAS')
    plt.show()
    
def mostra_grafico2():
    dados  =  pd.read_csv('DataSete/interface_grafico.csv')
    plt.bar(figsize=(8,6))
    plt.pie(dados['vendas'],labels=dados['mes'], autopct='%1.1f%%')
    plt.title('VENDAS')
    plt.show()
       
def mostra_grafico3():
    dados  =  pd.read_csv('DataSete/interface_grafico.csv')
    plt.plot(figsize=(8,6))
    plt.pie(dados['vendas'],labels=dados['mes'], autopct='%1.1f%%')
    plt.title('VENDAS')
    plt.show()
    
def mostra_grafico4():
    dados  =  pd.read_csv('DataSete/interface_grafico.csv')
    plt.scarter(figsize=(8,6))
    plt.pie(dados['vendas'],labels=dados['mes'], autopct='%1.1f%%')
    plt.title('VENDAS')
    plt.show()
    

janela  = tk.Tk()
janela.geometry('500x500')
janela.configure(bg='red')


# text_box = tk.Text(font=('georgia', 16))
# text_box.pack()


texto =  tk.Label(text= 'GERE GRAFICOS', font=('arial', 16))
texto.pack(pady= 20)


# 3  botões 


btn  =  tk.Button(janela, text= 'clique aqui', font=('arial', 16), command=mostra_grafico)
btn.pack(pady=20)

btn2  =  tk.Button(janela, text= 'clique aqui', font=('arial', 16), command=mostra_grafico2)
btn2.pack(pady=20)

btn3  =  tk.Button(janela, text= 'clique aqui', font=('arial', 16), command=mostra_grafico3)
btn.pack(pady=20)

btn4 =  tk.Button(janela, text= 'clique aqui', font=('arial', 16), command=mostra_grafico4)
btn.pack(pady=20)










janela.mainloop()