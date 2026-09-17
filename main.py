#Esquelo Projeto BILHETERIA   
lista_inscricao = []
 
# CREATE
 
nome = input("Digite seu nome: ")                    
Idade = input("Digite sua idade: ")                    
Poltrona = input ("Numero da poltrona solicitada: ")                   
status_inscricao = 'Confirmado'      
 
nova_inscricao = {
    'nome': nome,
    'idade': Idade,
    'poltrona': Poltrona,
    'status_inscricao': status_inscricao
}
 
lista_inscricao.append(nova_inscricao)
 
print(lista_inscricao)
 
 
#READ/IMPRIMIR
 
for inscricao in lista_inscricao:    
    print(f'Nome: {inscricao['nome']}\nIdade: {inscricao['idade']}\nPoltrona: {inscricao['poltrona']}\nStatus: {inscricao['status_inscricao']}')
 
 
# UPDATE
 
#("Quem? O que?")
 
# Exemplo: alterar a idade:
 
nome_alterado = input('Digite o nome da inscriçao a ser alterado: ')      #Input quem quer alterar
nova_idade = input('Digite a nova idade: ')   #Input nova idade
poltrona_alterada = input('Digite o número da poltrona alterada: ')   #Input nova poltrona
 
for inscricao in lista_inscricao:
    if nome_alterado == inscricao['nome']:
        inscricao['idade'] = nova_idade
        inscricao['poltrona'] = poltrona_alterada
 
 
#Você pode fazer um FOR para alterar qualquer coisa do dicionário
 
# DELETE
 
 
nome_deletado = input('Digite o nome da inscrição a ser deletada: ')   #Input quem quer deletar
 
for inscricao in lista_inscricao:
    if nome_deletado == inscricao['nome']:
        lista_inscricao.remove(inscricao)
 
 