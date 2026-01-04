```py

from time import sleep
from random import randint


lista = ["Pedra", "Papel", "Tesoura"]
print('[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] Tesoura')

while True:
    try:
        escolha = int(input('Escolha (0-2): '))
        if 0 <= escolha <= 2:
            break  # SAI do loop se válido
        print("Inválido! Digite 0, 1 ou 2")
    except ValueError:
        print("Digite apenas números!")

print('-'*19)

print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
sleep(2)

print('-'*19)

aleatorio = randint(0, 2)    # 1º: cria a variável
jogadapc = aleatorio         # 2º: copia o valor
jogada_pc_texto = lista[aleatorio] # texto: "Pedra"/"Papel"/"Tesoura"
jogada_jogador_texto = lista[escolha]

print(f'Sua escolha foi: {jogada_jogador_texto}')

if escolha == jogadapc:
  print(f'Minha escolha foi {jogada_pc_texto}, Temos um EMPATE!')
elif (escolha == 0 and jogadapc == 2) or \
     (escolha == 1 and jogadapc == 0) or \
     (escolha == 2 and jogadapc == 1):
     print(f'Minha escolha foi {jogada_pc_texto}, Você ganhou!!')
else:
    print(f'Minha escolha foi {jogada_pc_texto}, Você perdeu!!')

```
