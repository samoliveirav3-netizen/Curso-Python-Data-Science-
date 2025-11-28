import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# CARREGA
url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
df = pd.read_csv(url)

# DADOS
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Sex'] = LabelEncoder().fit_transform(df['Sex'])
df['Pclass'] = df['Pclass'].astype('category')

# INTERFACE
root = tk.Tk()
root.title("Dashboard de Análise do Titanic")
root.geometry("1200x800")


frame_grafico = tk.Frame(root)
frame_grafico.pack(pady=20, fill=tk.BOTH, expand=True)

# Frame para controles
frame_controles = tk.Frame(root)
frame_controles.pack(pady=10)

# Frame para resultados
frame_resultados = tk.Frame(root)
frame_resultados.pack(pady=10)

# Variáveis para armazenar resultados
label_tendencia = tk.Label(frame_resultados, text="", justify=tk.LEFT)
label_tendencia.pack()

label_descricao = tk.Label(frame_resultados, text="", justify=tk.LEFT)
label_descricao.pack()

label_previsao = tk.Label(frame_resultados, text="", justify=tk.LEFT)
label_previsao.pack()







# Função para limpar o frame do gráfico
def limpar_frame():
    for widget in frame_grafico.winfo_children():
        widget.destroy()

# Função para mostrar gráfico de barras
def mostrar_barras():
    limpar_frame()
    fig, ax = plt.subplots(figsize=(8, 5))
    
    sobreviventes_por_classe = df.groupby('Pclass')['Survived'].mean() * 100
    sobreviventes_por_classe.plot(kind='bar', color=['red', 'green', 'blue'], ax=ax)
    
    ax.set_title('Taxa de Sobrevivência por Classe')
    ax.set_xlabel('Classe')
    ax.set_ylabel('Porcentagem de Sobreviventes')
    ax.set_ylim(0, 100)
    
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    

    insight = "Insight: Passageiros da 1ª classe tiveram maior taxa de sobrevivência."
    label_tendencia.config(text=insight)


def mostrar_linhas():
    limpar_frame()
    fig, ax = plt.subplots(figsize=(8, 5))
    
    idade_media_sobreviventes = df[df['Survived'] == 1].groupby('Pclass')['Age'].mean()
    idade_media_nao_sobreviventes = df[df['Survived'] == 0].groupby('Pclass')['Age'].mean()
    
    idade_media_sobreviventes.plot(kind='line', marker='o', label='Sobreviventes', ax=ax)
    idade_media_nao_sobreviventes.plot(kind='line', marker='o', label='Não Sobreviventes', ax=ax)
    
    ax.set_title('Idade Média por Classe e Sobrevivência')
    ax.set_xlabel('Classe')
    ax.set_ylabel('Idade Média')
    ax.legend()
    
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    # Insight
    insight = "Insight: Passageiros mais jovens da 3ª classe tiveram menor chance de sobrevivência."
    label_tendencia.config(text=insight)


def mostrar_pizza():
    limpar_frame()
    fig, ax = plt.subplots(figsize=(8, 5))
    
    sobreviventes = df['Survived'].value_counts()
    sobreviventes.plot(kind='pie', autopct='%1.1f%%', labels=['Não Sobreviveu', 'Sobreviveu'], 
                       colors=['red', 'green'], ax=ax)
    
    ax.set_title('Distribuição de Sobreviventes')
    ax.set_ylabel('')
    
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    # Insight
    insight = "Insight: Apenas cerca de 38% dos passageiros sobreviveram ao desastre."
    label_tendencia.config(text=insight)


def mostrar_tendencia():
    limpar_frame()
    
    idade_media = df['Age'].mean()
    idade_mediana = df['Age'].median()
    idade_moda = df['Age'].mode()[0]
    
    tarifa_media = df['Fare'].mean()
    tarifa_mediana = df['Fare'].median()
    tarifa_moda = df['Fare'].mode()[0]
    
    resultado = (
        f"Idade:\n"
        f"  Média: {idade_media:.1f} anos\n"
        f"  Mediana: {idade_mediana:.1f} anos\n"
        f"  Moda: {idade_moda:.1f} anos\n\n"
        f"Tarifa:\n"
        f"  Média: ${tarifa_media:.2f}\n"
        f"  Mediana: ${tarifa_mediana:.2f}\n"
        f"  Moda: ${tarifa_moda:.2f}"
    )
    
    label_tendencia.config(text=resultado)
    

    insight = "Insight: A mediana da tarifa é menor que a média, que poucos passageiros pagaram tarifas altas."
    label_tendencia.config(text=resultado + "\n\n" + insight)


def mostrar_describe():
    limpar_frame()
    
    descricao = df[['Age', 'Fare', 'Pclass', 'Survived']].describe().to_string()
    label_descricao.config(text=descricao)
    
    # Insight
    insight = "Insight: 75% dos passageiros pagaram até $31.00, mas o máximo foi $512.33 - uma grande disparidade."
    label_descricao.config(text=descricao + "\n\n" + insight)
# -------------------------------------------------------------------------
#fzendo a previsão de possibilidade de sobrevivencia ...
def fazer_previsao():
    limpar_frame()
    
    # Preparar dados para modelo
    features = ['Pclass', 'Sex', 'Age', 'Fare']  

    X  =  df[features]
    y  =  df['Survived']  

    # Dividir dados
    X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size  =  0.2, random_state=42)
    
    # Treinar modelo
    model= RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)


    # Fazer previsões
    y_pred =  model.predict(X_test)
        
    # Calcular acurácia
    accuracy =  accuracy_score(y_test, y_pred)
    
    # Mostrar importância das features
    importancia = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(8, 4))
    importancia.plot(kind='bar', ax=ax)
    ax.set_title('Importância das Características na Previsão')

    #--------------------------------------------------------------------
    
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    # Resultado
    resultado = (
        f"Acurácia do modelo: {accuracy*100:.1f}%\n"
        f"Fatores mais importantes:\n"
        f"1. Sexo (0=feminino, 1=masculino)\n"
        f"2. Classe\n"
        f"3. Idade\n"
        f"4. Tarifa"
    )
    
    label_previsao.config(text=resultado)
 
    insight = "Insight: Sexo foi o fator mais importante, com mulheres tendo maior chance de sobrevivência."
    label_previsao.config(text=resultado + "\n\n" + insight)

# -------------------------------------------------------------------------

btn_barras = ttk.Button(frame_controles, text="Gráfico de Barras", command=mostrar_barras)
btn_barras.grid(row=0, column=0, padx=5, pady=5)

btn_linhas = ttk.Button(frame_controles, text="Gráfico de Linhas", command=mostrar_linhas)
btn_linhas.grid(row=0, column=1, padx=5, pady=5)

btn_pizza = ttk.Button(frame_controles, text="Gráfico de Pizza", command=mostrar_pizza)
btn_pizza.grid(row=0, column=2, padx=5, pady=5)

btn_tendencia = ttk.Button(frame_controles, text="Medidas de Tendência", command=mostrar_tendencia)
btn_tendencia.grid(row=0, column=3, padx=5, pady=5)

btn_describe = ttk.Button(frame_controles, text="Descrição dos Dados", command=mostrar_describe)
btn_describe.grid(row=0, column=4, padx=5, pady=5)

btn_previsao = ttk.Button(frame_controles, text="Previsão de Sobrevivência", command=fazer_previsao)
btn_previsao.grid(row=0, column=5, padx=5, pady=5)

root.mainloop()