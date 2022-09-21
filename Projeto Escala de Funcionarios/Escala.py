import os

def Pergunta_Principal():
    EscolhaPrincipal = int(input("1 - Adicionar Funcionario""\n""2 - Retirar Funcionario""\n""3 - Gerar escala""\n""4 - Sair""\n"))

    if EscolhaPrincipal == 1:
        os.system("cls")
        Adicionar_Funcionario()

    elif EscolhaPrincipal == 2:
        os.system("cls")
        Retirar_Funcionario()

    elif EscolhaPrincipal == 3:
        os.system("cls")
        Gerar_Escala()

    elif EscolhaPrincipal == 4:
        exit()

    elif EscolhaPrincipal != "1" and "2" and  "3" and "4":
        print("Opcao invalida")


def Adicionar_Funcionario():
    global Horario_Adicionar
    Horario_Adicionar = int(input("Escolha um Horario:""\n""1 - Horario das 06:50""\n""2 - Horario das 08:00""\n""3 - Horario das 09:00""\n""4 - Voltar""\n"))
    
    if Horario_Adicionar == 1:
        os.system("cls")
        print("Em producao")


    elif Horario_Adicionar == 2:
        os.system("cls")
        print("Em producao")

    elif Horario_Adicionar == 3:
        os.system("cls")
        print("Em producao")

    elif Horario_Adicionar == 4:
        os.system("cls")
        print(10*"-","Bem vindo ao gerador de escalas",10*"-")
        return Pergunta_Principal()



def Retirar_Funcionario():
    global Horario_Retirar
    Horario_Retirar = int(input("Escolha um Horario:""\n""1 - Horario das 06:50""\n""2 - Horario das 08:00""\n""3 - Horario das 09:00""\n""4 - Voltar""\n"))
    if Horario_Retirar == 1:
        os.system("cls")
        print("Em producao")

    elif Horario_Retirar == 2:
        os.system("cls")
        print("Em producao")

    elif Horario_Retirar == 3:
        os.system("cls")
        print("Em producao")

    elif Horario_Retirar == 4:
        os.system("cls")
        print(10*"-","Bem vindo ao gerador de escalas",10*"-")
        return Pergunta_Principal()


def Gerar_Escala():
    print("Em producao")






print(10*"-","Bem vindo ao gerador de escalas",10*"-")
Pergunta_Principal()