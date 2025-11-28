import minhas_funcoes_8
while True:
    print("Sistema de notas(Moda,Media,Mediana,Varianca,Desvio Padrão):")
    aluno =["Samuel", "Pedro"]
    nota = [[6,8,9],[7,5,10]]
    Samuel = nota[0]
    Pedro = nota[1]
    a = input(""""""
          
    "1 - Ver Alunos" 
    "2 - Sistema de Notas"
    "3 - Sair"  
          
          """""")
    if a == "1":
        print(aluno)
        print(nota)
    elif a == "2":
        alunos = input("Qual aluno deseja:")
        i = aluno.index(alunos)
        minhas_funcoes_8.m_media(nota[i])
        minhas_funcoes_8.m_mediana(nota[i])
        minhas_funcoes_8.m_moda(nota[i])
        minhas_funcoes_8.m_varianca(nota[i])
        minhas_funcoes_8.m_desvio_padrao(nota[i])
        minhas_funcoes_8.m_mn(nota[i])
        minhas_funcoes_8.m_men(nota[i])
    elif a == "3":
        print("Encerrando!")
    else:
        print("Errado")    


