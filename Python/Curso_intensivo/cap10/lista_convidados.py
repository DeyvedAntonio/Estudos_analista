# Exercício 10.4

while True:
    nome_usuario = input('Qual é o nome do usuário: ')
    print(f'Seja bem vindo {nome_usuario}!')
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(f'visita do usuario {nome_usuario}.\n')
