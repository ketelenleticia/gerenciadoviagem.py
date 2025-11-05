from tabulate import tabulate
listaViagens=[]
def registrar_viagem(listaViagens):
    nome=input("digite o nome do motorista: ")
    destino=input("digite o seu destino: ")
    distancia=float(input("digite a sua distancia: "))
    combustivel=float(input("digite o seu combustivel: "))
    consumo=combustivel/distancia
     
    listaViagens.append ({
        "nome": nome,
        "destino": destino,
        "distancia":distancia,
        "combustivel":combustivel,
        "consumo": consumo
    })

    print(listaViagens)

def exibir_viagens(listaViagens) :
    if not listaViagens:
        print("nao a viagens registradas")
    else:    
        tabela = []
        for a in listaViagens:
            tabela.append([a["nome"],  a["destino"], a["distancia"],a["combustivel"],a["consumo"]])

            print(" RELATÓRIO DE VIAGENS")
            print(tabulate(
                tabela,
                headers=["nome", "destino", "distancia","combustivel","consumo"],
                tablefmt="fancy_grid"
            ))
def buscar_motorista(listaViagens):
    nomemot=input("digite nome do motorista: ")
    for i in listaViagens:
         if i["nome"].lower()== nomemot.lower():
             exibir_viagens(listaViagens)
         else:
             print("nenhuma viagem encontrada")    

def  viagem_mais_cara(listaViagens):
    if not listaViagens:
         print("nenhuma")
         return
     for v in listaViagens:
         viagem_cara= max(listaViagens, key=lambda v :v["combustivel"])
         print(f"o item com maior gasto de consumo: {viagem_cara["combustivel"]} da viagem {viagem_cara["destino"]}")

