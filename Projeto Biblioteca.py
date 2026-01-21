
print('Bem vindo a Biblioteca :')
#Funções # Lista vazia
lista_livros = []
id_global = 5618715 #Pode ser um contador de livro

#Funções do Codigo
def cadastrar_livro(id):
    nomeLivro = input('Informe o nome do livro: ')
    editoraLivro = input('Informe a editora do livro: ')
    autorLivro = input('Informe o autor do livro: ')
    
    dioconarioLivro = {'id': id, 'nome': nomeLivro, 'autor': autorLivro,  'editora' : editoraLivro}
    
    lista_livros.append(dioconarioLivro.copy())

def consultar_livros() -> None:
    while True:
       print('1 - Consultar todos os livros')
       print('2 - Consultar livros por Id')
       print('3 - Consultar os livros por editora')
       print('4 - Consultar os livros por autor')
       print('5 - Sair')
       opc = input('>>')
       match opc:
          case '1':
             for livro in lista_livros:
               for chave, valor in livro.items():
                   print(f'{chave}: {valor}')
                   print()
          case '2': 
               id_consulta = int(input('Informe o ID a ser consultado: '))
               for livro in lista_livros:
                  if livro ['id'] == id_consulta:
                   for chave, valor in livro.items():
                    print(f'{chave}: {valor}')
                    print()
          case '3':
              editora_consulta = input('Informe a editora a ser consultada:')
              for livro in lista_livros:
                if livro ['editora'] == editora_consulta:
                  for chave, valor in livro.items():
                   print(f'{chave}: {valor}')
                   print()
          case '4':
              autor_consulta = input('Informe o autor a ser consultado:')
              for livro in lista_livros:
                if livro ['autor'] == editora_consulta:
                  for chave, valor in livro.items():
                    print(f'{chave}:{valor}')
                  print()  
                                
          case '5':
            return        

def remove_livro():
  while True:
    id_remove = int(input('Informe o id a ser removido:'))
    for livro in lista_livros:
       if livro['id'] == id_remove:
        print(f'O Livro {livro['nome']}', end='' ) 
        lista_livros.remove(livro) 
        print('Livro removido com sucesso')
        return
    print('Id não encontrado')             
       
    
#Programa principal - usando laço de repetição    
    #Menu opções:
while True:
   print('1 -> Cadastrar livro: ')
   print('2 -> Consultar livro:')
   print('3 -> Remover livro: ')
   print('4 -> Sainda do Biblioteca...')
   opc = input(">>>")
   match opc:
    case '1':
       cadastrar_livro(id_global)
       id_global += 1
    case '2':
       consultar_livros() 
       print(lista_livros)
    case '3':
      remove_livro()
    case '4':
      break 
    case _:
      print('Opção invalida')   
#match case em Python (a partir da versão 3.10) é uma estrutura de controle de fluxo para correspondência de padrões (pattern matching), mais poderosa que o if-elif-else, permitindo comparar uma expressão com vários padrões (valores, sequências, classes) e executar código, com o case _ funcionando como um else genérico, ideal para código mais limpo e legível, especialmente com dados complexos.        
       