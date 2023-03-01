# Exercício 10.3

nome_usuario = input('Digite um nome de usuário: ')
with open('guest.txt', 'a') as file_object:
    file_object.write(f'{nome_usuario}\n')
