#Esquelo Projeto BILHETERIA   
lista_inscricao = []
 
# CREATE
 
nome = input("Digite seu nome: ")                    
Idade = input("Digite sua idade: ")                    
Poltrona = input ("Numero da poltrona solicitada: ")                   
status_inscricao = 'Confirmado'      
 
nova_inscricao = {
    'nome': nome,
    'curso': curso,
    'carga_horaria': carga_horaria,
    'status_inscricao': status_inscricao
}
 
lista_inscricao.append(nova_inscricao)
 
print(lista_inscricao)
 
 
#READ/IMPRIMIR
 
for inscricao in lista_inscricao:    
    print(f'Nome: {inscricao['nome']}\nCurso: {inscricao['curso']}\nCarga Horária: {inscricao['carga_horaria']}\nStatus: {inscricao['status_inscricao']}')
 
 
# UPDATE
 
#("Quem? O que?")
 
# Exemplo: alterar o curso:
 
nome_aluno = 'Raphael'      #Input quem quer alterar
novo_curso = 'artesanato'   #Input novo curso
carga_horaria = 5
 
for inscricao in lista_inscricao:
    if nome_aluno == inscricao['nome']:
        inscricao['curso'] = novo_curso
 
 
#Você pode fazer um FOR para alterar qualquer coisa do dicionário
 
# DELETE
 
 
nome_aluno = 'Raphael'   #Input quem quer deletar
 
for inscricao in lista_inscricao:
    if nome_aluno == inscricao['nome']:
        lista_inscricao.remove(inscricao)
 
 