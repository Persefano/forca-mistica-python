import math
import random
lista = [1,1000]
a = random.randint(100,1000)
print('NIVÉL DE FORCA: {}'.format(a))
raiz_quadrada = math.pow(a, 1/2)
raiz_cubica = math.pow(a,1/3)
print('FORÇA AUMENTADA EM: {:.2f}%'.format(raiz_quadrada))
print('FORÇA DIMINUIDA EM: {:.2f}%'.format(raiz_cubica))
#A maquina escolhe um número aleatório.
#O resultado revela a raiz quadrada e cúbica do número.



