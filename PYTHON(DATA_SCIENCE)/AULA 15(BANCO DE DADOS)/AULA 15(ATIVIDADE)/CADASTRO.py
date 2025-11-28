import sqlite3
import pandas as pd
import matplotlib.pyplot as plt 
import tkinter as tk
import numpy as np
import customtkinter
from tkinter import messagebox


def banco():
    # 1 criar o arquivo
    return  sqlite3.connect('dados.db')
  

def tabela():
    conn =  banco()
    c  =  conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuario(
     
             nome TEXT,
             idade INTEGER,
             salario REAL,
             regiao TEXT          
    
            )''')
    conn.commit()
    conn.close()        


def inserir():
    conn =  banco()
    c  =  conn.cursor()

    nome  =  nome_entry.get()
    idade = idade_entry.get()
    salario = salario_entry.get()
    regiao = regiao_entry.get()
    
    if nome and idade and salario and regiao: 
        c.execute('INSERT INTO usuario VALUES(?,?,?,?)',(nome, idade, salario, regiao))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'DADOS INSERIDOS COM SUCESSO!')
        
    else: 
        messagebox.showerror('', 'ERRO AO INSERIR')    
           

def organize():
    
    conn =  banco()
    c  =  conn.cursor()


    d = {
    
    'nomes':[],
    'idades':[],
    'salarios':[],
    'regiões':[]

    } 

    c.execute('SELECT  * FROM usuario')
    dados  =  c.fetchall()
    
    for infos in dados:
        for nome in infos:
            pass
        d['nomes'].append(infos[0])

    
    for infos in dados:
        for idade in infos:
            pass
        d['idades'].append(infos[1])
   
    for infos in dados:
        for salario in infos:
            pass
        d['salarios'].append(infos[2])


    for infos in dados:
        for regiao in infos:
            pass
        d['regiões'].append(infos[3])
   
    print(d['salarios'])
    
    df  =  pd.DataFrame(d)
    df.to_csv('DADOS_SALARIO.csv', index = False)

    df =  pd.read_csv('DADOS_SALARIO.csv')


    plt.figure(figsize = (10,8))
    plt.plot(df['salarios'], df['regiões'])
    plt.title('GRAFICO DE LINHA')
    plt.xlabel('SALARIOS')
    plt.xlabel('REGIÕES')
    plt.show()



root  =  customtkinter.CTk()
root.configure(fg_color = 'orange' )
# root.geometry('750x600')
ima =  'IMAGEM.ico'
root.iconbitmap(ima)

root.title('CARREGAR DADOS')

customtkinter.CTkLabel(root, text  =  'Formulário de cadastro' , font=('arial', 25), fg_color = 'orange').grid(pady = 10)

customtkinter.CTkLabel(root, text  =  '------------------------------------------' , font=('arial', 12), fg_color = 'orange').grid(pady = 10)

customtkinter.CTkLabel(root, text  =  'Nomes' , font=('arial', 18)).grid(pady = 10)

nome_entry = customtkinter.CTkEntry(root, font=('arial', 18))
nome_entry.grid()

customtkinter.CTkLabel(root, text  =  'Idade' , font=('arial', 18)).grid(pady = 10)

idade_entry = customtkinter.CTkEntry(root, font=('arial', 18))
idade_entry.grid()

customtkinter.CTkLabel(root, text  =  'Salario' , font=('arial', 18)).grid(pady = 10)

salario_entry = customtkinter.CTkEntry(root, font=('arial', 18))
salario_entry.grid()

customtkinter.CTkLabel(root, text  =  'Região' , font=('arial', 18)).grid(pady = 10)

regiao_entry = customtkinter.CTkEntry(root, font=('arial', 18))
regiao_entry.grid()


btn =  customtkinter.CTkButton(root, text = 'salvar',font=('arial', 18), command = inserir)
btn.grid(pady = 10)


btn =  customtkinter.CTkButton(root, text = 'gerar', font=('arial', 12), command =  organize)
btn.grid(pady = 10)


tabela()


root.mainloop()







