import random
import math

heroi = ['Fogo em Chamas', 'Raio de SOL', 'Luz Do Caminho']
nome_aleatorio = random.choice(heroi)
print('Sorteou: ', nome_aleatorio)

poder = random.randint(10,100)
print('Poder: ', poder)

calculada = poder*1000
forca = math.pow(calculada, 0.5)
print('Força Calculada: {:.2f}' .format(forca))
