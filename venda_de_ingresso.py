ingressos = []


while True:
    print("\nEscolha uma opção:")
    print("\n[1] Ingresso, \n[2 ]Arrecadações, \n[3] Cancelamento, \n[4] Alterar poltrona, \n[5] Cancelar ingresso, \n[0] Sair")
    opcao = input("Digite uma Opção: ")
    
    if opcao == "1":
        nome = input("Digite seu nome: ")                    
        idade = input("Digite sua idade: ")  
        poltrona = input ("Numero da poltrona solicitada: ")
        qtd_ingressos = input("Digite quantos ingressos deseja comprar: ")  
        filme = input("Digite qual filme deseja assitir: ")

        ingresso = {'nome': nome, 'idade': idade, 'filme': filme, 'poltrona': poltrona, 'qtd_ingressos': qtd_ingressos, 'filme': filme}
        
        ingressos.append(ingressos)   
    elif opcao == "2":
         for ingresso in ingressos:
            print(f"{ingresso['nome']} | {ingresso['idade']}  | {ingresso['poltrona']} | {ingresso['qtd_ingressos']} | {ingresso['filme']}")
    
    elif opcao == "3":
        for ingresso in ingressos:
            nome = input("Digite seu nome: ")
            nova_poltrona = input("Digite a nova poltrona: ")
            for ingresso in ingressos:
                    if ingresso['nome'] == nome:
                        ingresso['poltrona'] = nova_poltrona
    elif opcao == "4":
        nome = input("Digite seu nome: ")
        for ingresso in ingressos:
            if ingresso['nome'] == nome:
                ingressos.remove(ingresso)
    elif opcao == "5":
        nome = input("Digite seu nome: ")
        for ingresso in ingressos:
            if ingresso['nome'] == nome:
                ingressos.remove(ingresso)
    else:
        break