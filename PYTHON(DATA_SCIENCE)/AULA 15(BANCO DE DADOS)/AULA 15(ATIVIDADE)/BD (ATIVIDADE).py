import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt


def definir_banco():
    return  sqlite3.connect('meu_banco_de_dados.db')

def tabela():
    conexao =  definir_banco()
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (

            id INTEGER,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            cidade TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()



# Criar a função que vai inserir os dados no banco de dados
# Crie abaixo desta linha:
def inserir_dados():
    conexao =  definir_banco()
    cursor = conexao.cursor()
    
    id_  =  entrada_id.get()
    nome  =  entrada_nome.get()
    idade  =  entrada_idade.get()
    cidade  =  entrada_cidade.get()
 
    if id_ and nome and idade and cidade:   
        cursor.execute('INSERT INTO pessoas VALUES(?,?,?,?)', (id_,nome,idade,cidade))
        messagebox.showinfo('', 'DADOS INSERIDOS COM SUCESSO!')
        conexao.commit()
        conexao.close()
    else: 
        messagebox.showerror('','INSIRA TODOS OS DADOS!')    



# Função para exibir dados em um gráfico
def exibir_grafico():
    conexao =  definir_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT nome, idade FROM pessoas')
    dados = cursor.fetchall()
    
    if dados:
        nomes = [dado[0] for dado in dados]
        idades = [dado[1] for dado in dados]

        plt.figure(figsize=(10, 5))
        plt.bar(nomes, idades, color='skyblue')
        plt.xlabel('Nome')
        plt.ylabel('Idade')
        plt.title('Idade das Pessoas')
        plt.show()
    else:
        messagebox.showwarning("Erro", "Nenhum dado encontrado para exibir.")





# Criar a janela principal
janela = tk.Tk()
janela.title("Cadastro de Pessoas")

tk.Label(janela, text="ID:").grid(row=0, column=0, padx=10, pady=5)
entrada_id = tk.Entry(janela)
entrada_id.grid(row=0, column=1, padx=10, pady=5)


# Rótulos e campos de entrada
tk.Label(janela, text="Nome:").grid(row=1, column=0, padx=10, pady=5)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Idade:").grid(row=2, column=0, padx=10, pady=5)
entrada_idade = tk.Entry(janela)
entrada_idade.grid(row=2, column=1, padx=10, pady=5)

tk.Label(janela, text="Cidade:").grid(row=3, column=0, padx=10, pady=5)
entrada_cidade = tk.Entry(janela)
entrada_cidade.grid(row=3, column=1, padx=10, pady=5)

# Botões
btn_inserir = tk.Button(janela, text="Inserir Dados", command = inserir_dados)
btn_inserir.grid(row = 4, column=0, columnspan=2, pady=10)

btn_grafico = tk.Button(janela, text="Exibir Gráfico", command=exibir_grafico)
btn_grafico.grid(row=5, column=0, columnspan=2, pady=10)


tabela()
janela.mainloop()




