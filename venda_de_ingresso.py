ingressos = []


while True:
    print("\nEscolha uma opção:")
    print("\n[1] Ingresso, \n[2 ]Listar Ingressos, \n[3] Alterar poltrona, \n[4] Cancelamento, \n[5] Atualizar ingresso \n[0] Sair")
    opcao = input("Digite uma Opção: ")
    
    if opcao == "1":
        nome = input("Digite seu nome: ")                    
        idade = input("Digite sua idade: ")  
        poltrona = input ("Numero da poltrona solicitada: ")
        qtd_ingressos = input("Digite quantos ingressos deseja comprar: ")  
        filme = input("Digite qual filme deseja assitir: ")

        ingresso = {
            'nome': nome, 
            'idade': idade,
            'filme': filme,
            'poltrona': poltrona,
            'qtd_ingressos': qtd_ingressos,
            'filme': filme
        }
        
        
        ingressos.append(ingresso)   
        print("Ingresso cadastrado com sucesso!")

    elif opcao == "2":
            if not ingressos:
                    print("\nNenhum ingresso cadastrado!")
            else:
                print("Eu existo")
                for ingresso in ingressos:
                    print(f"{ingresso['nome']} | {ingresso['idade']}  | {ingresso['poltrona']} | {ingresso['qtd_ingressos']} | {ingresso['filme']}")
                continue


    elif opcao == "3":
          nome_busca = input("Digite o nome do comprador: ")
          encontrado = False
          for ingresso in ingressos:
            if ingresso['nome'] == nome_busca:
                nova_poltrona = input("\nDigite a nova poltrona: ")
                ingresso['poltrona'] = nova_poltrona
                print("\nPoltrona alterada com sucesso!")
                encontrado = True
                break

            if not encontrado:
                print("\nComprador não encontrado.")

    elif opcao == "4":
        nome_busca = input("Digite o nome do comprador para cancelar o ingresso: ")
        encontrado = False
        for ing in ingressos:
            if ing['nome'] == nome_busca:
                ingressos.remove(ing)
                print("\nIngresso cancelado com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("\nComprador não encontrado.")

    elif opcao == "5":
         nome_busca = input("Digite o nome do comprador que deseja atualizar: ")
         encontrado = False
         for ingresso in ingressos:
            if ingresso['nome'] == nome_busca:
                print(f"\nComprador encontrado! Digite os novos dados (ou aperte Enter para manter se preferir):")
                
                novo_nome = input(f"Novo nome [{ingresso['nome']}]: ")
                nova_idade = input(f"Nova idade [{ingresso['idade']}]: ")
                novo_filme = input(f"Novo filme [{ingresso['filme']}]: ")
                nova_poltrona = input(f"Nova poltrona [{ingresso['poltrona']}]: ")
                nova_qtd = input(f"Nova quantidade [{ingresso['qtd_ingressos']}]: ")

                # Se o usuário digitar algo, atualiza; senão, mantém o valor antigo
                if novo_nome:
                    ingresso['nome'] = novo_nome
                if nova_idade:
                    ingresso['idade'] = nova_idade
                if novo_filme:
                    ingresso['filme'] = novo_filme
                if nova_poltrona:
                    ingresso['poltrona'] = nova_poltrona
                if nova_qtd:
                    ingresso['qtd_ingressos'] = nova_qtd

                print("\nIngresso atualizado com sucesso!")
                encontrado = True
                break
            
    elif opcao == "0":
        print("\nSaindo do sistema")
        break