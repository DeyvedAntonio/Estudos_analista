# Exercício 10.5

prompt = 'Por que você gosta de programação? '
prompt += '\n(Para sair escreva sair.) '
while True:
    msg = input(prompt)
    if msg.lower() == 'sair':
        break
    with open('enquete_programacao.txt', 'a') as file_object:
        file_object.write(f'{msg}\n')
