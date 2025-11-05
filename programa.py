from funçoes import *
def menu():
    listaViagens=[]
    while True:
        
        print("biblioteca de livros")
        print("1- Registra nova viagem")
        print("2- Exibir de todas viagens") 
        print("3- Buscar viagem por motoristas")
        print("4- Exibir viagem mais cara")
        print("5- Mostrar media geral de consumo") 
        print("0- Encerra o programa")

        opçao=input("escolha uma opçao: ") 

        if opçao =="1":
           registrar_viagem(listaViagens)
        elif  opçao=="2":
             exibir_viagens(listaViagens)
        elif opçao=="3" :
             buscar_motorista(listaViagens)
        elif opçao=="4" :
             viagem_mais_cara(listaViagens)
        elif opçao=="5":  
             media_consumo(listaViagens)

        elif opçao=="0":
            print("fim")
            break
menu()        