# \n






IDADE_MINIMA = 18
cliente = int(input('Digite sua idade: \n' ))
bebidas = 0 


if cliente >= IDADE_MINIMA:
    print('Acesso permitido, será direcionado ao cardápio do bar.')
    if cliente >= IDADE_MINIMA:
        bebidas = int(input("Qual bebida deseja consumir: Wiskhy=1,Vodka=2, Cerveja=3, Refrigerante=4 \n"))
        print(bebidas)
else:
    print('Acesso negado, por favor se retire!')
    exit()
    
    

comanda = bool(input("Digite True, para concluir a compra, digite False para cancelar a compra."))

if bebidas ==1:
    print("O valor do Whisky é de R$20,00, deseja confirmar o pedido? \n", comanda)
    if comanda == True:
        print("Compra realizada no valor de R$20,00 \n")
    elif comanda == False:
        print("Compra não efetuada, necessário consumação no local \n")
elif bebidas ==2:
    print("O valor da Vodka é de R$15,00, deseja confirmar o pedido? \n", comanda)
    if comanda == True:
        print("Compra realizada no valor de R$15,00 \n")
    elif comanda == False:
        print("Compra não efetuada, necessário consumação no local \n")

elif bebidas == 3 :
    print("O valor da Cerveja é de R$5,00 a lata, deseja confirmar o pedido? \n", comanda)
    if comanda == True:
        print("Compra realizada no valor de R$5,00 \n")
    elif comanda == False:
        print("Compra não efetuada, necessário consumação no local \n")

elif bebidas == 4:
    print("O valor do Refrigerante é de R$5,00 a lata, deseja confirmar o pedido? \n", comanda)
    if comanda == True:
        print("Compra realizada no valor de R$5,00 \n")
    elif comanda == False:
        print("Compra não efetuada, necessário consumação no local \n")
else:
    print("É necessário consumação no ambiente, retornar a escolha de bebidas\n")
