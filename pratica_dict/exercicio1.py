# Sistema de perguntas e respostas usando dictionaries.

perguntas = [
    {
        'pergunta' : 'Quanto é 2+2?',
        'escolhas' : ['1', '3', '4', '5'],
        'resposta' : '4',
    }
]

print(f'Pergunta: {perguntas[0]['pergunta']}')
print('Opções:')
print(f'0) {perguntas[0]['escolhas'][0]}')
print(f'1) {perguntas[0]['escolhas'][1]}')
print(f'2) {perguntas[0]['escolhas'][2]}')
print(f'3) {perguntas[0]['escolhas'][3]}')
resposta = int(input('Insira a respota: '))
if perguntas[0]['escolhas'][resposta] == perguntas[0]['resposta']:
    print('Você acertou')
else:
    print('Você errou')