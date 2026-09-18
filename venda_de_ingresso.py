

'''

ingressos = []

while true

MENU 
    1 VENDER INGRESSO
    2 IMPRIMIR
    3 CANCELAR/ALTERAR/DELETAR
    4 Alterar poltrona
    5 Cancelar ingresso
    0 SAIR

    opcao = input("Digite uma das opcoes acima": )
    
IF opcao == 1:

    variaveis = input 
    poltrona = input...
    preco =...
    nome = input("Digite o nome do comprador: ")
    filme = input("DIgite o nome do filme: )

    ingresso = {'nome': nome, 'filme': filme ...}

    ingressos.append(ingresso)

elif opcao == 2:
    for ingresso in ingressos:
        print(f'{ingresso['nome']}  | {ingresso['poltrona']}')


elif opcao == 3:
    for ingresso in ingressos:
        soma += ingresso['preco']

elif opcao == 4:
    nome = input (...)
    nova_poltrona = ....

    for ingresso in ingressos:
        if ingresso['nome'] == nome:
            ingresso['poltrona'] = nova_poltrona

loop for


    print(soma)
else:
    break



def vender_ingresso ():
    poltronas_disponiveis = 50
    preço_inteira = float(f"R$40")
    preço_meia = float(f"R$20")
'''
ingressos = []


while True:
    print("\nEscolha uma opção:")
    print("\n[1] Ingresso, \n[2 ]Arrecadações, \n[3] Cancelamento, \n[4] Alterar poltrona, \n[5] Cancelar ingresso, \n[0] Sair")
    opcao = input("Digite uma Opção: ")
    
    if opcao == 1:
        nome = input("Digite seu nome: ")                    
        idade = input("Digite sua idade: ")  
        poltrona = input ("Numero da poltrona solicitada: ")
        qtd_ingressos = input("Digite quantos ingressos deseja comprar: ")  
        filme = input("Digite qual filme deseja assitir: ")

        ingresso = {'nome': nome, 'idade': idade, 'filme': filme, 'poltrona': poltrona, 'qtd_ingressos': qtd_ingressos, 'filme': filme}
        
        ingressos.append(ingressos)   
    elif opcao == 2:
         for ingresso in ingressos:
        print (f"{ingresso['nome']} | {ingresso['idade']}  | {ingresso['poltrona']} | {ingresso[qtd_ingressos]} | {ingresso[filme]}")
    
    elif opcao == 3:
        for ingresso in ingressos:

    
    else:
        break