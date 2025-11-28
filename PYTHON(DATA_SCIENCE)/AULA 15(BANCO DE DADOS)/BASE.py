import tkinter  as tk
import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
from tkinter import messagebox
from tkinter import ttk


def banco():
    return  sqlite3.connect('banco.db')

def tabela():
    conn =  banco()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS vendas(

             vendedor TEXT,
             vendas REAL,
             mes TEXT,
             produto TEXT 
           
    
              )''')
    conn.commit()
    conn.close()          


def inserir():
    conn =  banco()
    c = conn.cursor()
    
    nome_vendedor =  nome_entry.get()
    vendas  =  venda_entry.get()
    mes  =  mes_entry.get()
    produto =  produto_entry.get()

    try:
    
        c.execute('INSERT INTO vendas VALUES(?,?,?,?)', (nome_vendedor, vendas, mes, produto))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'dados inseridos!')
    except:
        messagebox.showerror('', 'erro ao inserir!')


def criar_csv():
    conn =  banco()
    c = conn.cursor()
    c.execute('SELECT * FROM vendas')
    VENDAS = c.fetchall()
    # print(VENDAS)

    vendas_dados ={
    'vendedor':[],
    'venda':[],
    'mes':[],
    'produto':[]
    }

    for dados in VENDAS:
        vendas_dados['vendedor'].append(dados[0])
        vendas_dados['venda'].append(dados[1])
        vendas_dados['mes'].append(dados[2])
        vendas_dados['produto'].append(dados[3])
        
    print(vendas_dados)    
    
    df  =  pd.DataFrame(vendas_dados)
    df.to_csv('dados_vendas.csv', index = False)
    df.to_excel('dados_vendas.xlsx', index = False)
    df.to_json('dados.json')
    df.to_html('index.html')
    

def linha():
    criar_csv()
    dado =  pd.read_csv('dados_vendas.csv')
    df = pd.DataFrame(dado)

    media  =  df.groupby('produto')['venda'].mean()

     
    plt.figure(figsize = (10,8))
    plt.title('MEDIA DE VENDAS POR PRODUTO')
    media.plot(kind = 'line')

    plt.show()

def barras():
    criar_csv()
    dado =  pd.read_csv('dados_vendas.csv')
    df = pd.DataFrame(dado)

    media  =  df.groupby('vendedor')['venda'].mean()

     
    plt.figure(figsize = (10,8))
    plt.title('MEDIA DE VENDAS POR vendedor')
    media.plot(kind = 'bar')
    
    plt.show()


def barras():
    criar_csv()
    dado =  pd.read_csv('dados_vendas.csv')
    df = pd.DataFrame(dado)

    media  =  df.groupby('vendedor')['venda'].mean()

     
    plt.figure(figsize = (10,8))
    plt.title('MEDIA DE VENDAS POR vendedor')
    media.plot(kind = 'bar')
    
    plt.show()

def PIZZA():
    dado =  pd.read_csv('dados_vendas.csv')
    df = pd.DataFrame(dado)

    # media  =  df.groupby('mes')['venda'].sum()



     
    plt.figure(figsize = (10,8))
    plt.title('Vendas Mês')
    plt.pie(df['venda'], labels =  df['vendedor'], autopct = '%%1.f%%')
    
    plt.show()


def estatistica():
  
    dado =  pd.read_csv('dados_vendas.csv')
    df = pd.DataFrame(dado) 

    es = df.describe()
    esta.config(text = es)
 

janela   =  tk.Tk()
janela.geometry('1500x950')


tk.Label(janela, text =  'INSIGHT DE VENDAS E PRODUTOS', font=('arial', 15)).pack()
nome = tk.Label(janela, text = 'Vendedor: ', font=('arial', 15))
nome.pack()





vendedores_ = ["Mara", "Junior", "Cherry","Helio"]

# Combobox  
nome_entry = ttk.Combobox(janela, values=vendedores_)
# nome_entry.set("Select a fruit")
nome_entry.pack()





venda = tk.Label(janela, text = 'Venda:', font=('arial', 15))
venda.pack()

venda_entry = tk.Entry(janela)
venda_entry.pack()


meses = ['JAN','FEV', 'MAR', 'ABR', 'MAI', 'JUN']

mes = tk.Label(janela, text = 'Mês: ', font=('arial', 15))
mes.pack()

mes_entry = ttk.Combobox(janela, values=meses)
mes_entry.pack()

produto = tk.Label(janela, text = 'Produto: ', font=('arial', 15))
produto.pack()

lista_prod = ['MDF RIPADO', 'MDF BRANCO', 'MDF ACRILICO']

produto_entry = ttk.Combobox(janela, values=lista_prod)
produto_entry.pack()

btn_salvar  =  tk.Button(janela, text =  'Salvar', command = inserir, font=('arial', 15))
btn_salvar.pack(pady = 20)

btn_linha  =  tk.Button(janela, text =  'Grafico de linha', command =  linha, font=('arial', 15))
btn_linha.pack(pady = 20) 

btn_barras  =  tk.Button(janela, text =  'Grafico de barras', command =  barras, font=('arial', 15))
btn_barras.pack(pady = 20) 


btn_pizza  =  tk.Button(janela, text =  'Grafico de pizza', command =  PIZZA, font=('arial', 15))
btn_pizza.pack(pady = 20) 

btn_es  =  tk.Button(janela, text =  'Estatistica', command =  estatistica, font=('arial', 15))
btn_es.pack(pady = 20) 


esta = tk.Label(janela, text = 'Mostras a estatistica ', font=('arial', 15))
esta.pack()






tabela()
criar_csv()

janela.mainloop()