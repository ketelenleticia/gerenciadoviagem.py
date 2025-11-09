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
    viagem=[v for v in listaViagens if v["nome"].lower()==nomemot.lower()]
    
    if viagem:
      print(tabulate(viagem, headers="keys",tablefmt="grid"))

    else:
      print("nenhuma viagem encontrada")    

def  viagem_mais_cara(listaViagens):
     if not listaViagens:
         print("nenhuma")
         return
     else:
        viagem_cara=max(listaViagens,key=lambda v: v["combustivel"])
        print("viagem cara: ")
        print(tabulate([viagem_cara], headers="keys",tablefmt="grid"))

def media_consumo(listaViagens):
    if not listaViagens:
        print("nenhuma viagem registrada")  
        return
    media=sum(v["consumo"] for v in listaViagens)/len(listaViagens)
    print(f"a media geral de consumo: {media} R$/km")     
