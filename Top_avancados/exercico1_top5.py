
import numpy as np
'''
a = np.arange(1, 11)
print(a) #lista todos os numeros de 1 a 10
print(a.shape) # imprime o ultimo numero da lista 
print(a[::2]) #imprime todos os numeros impares da lista
print(a[::-1]) # lista os numeros em forma descrecente comecando por 10
print(a.sum()) # soma todos os numeros que estao na lista e imprime o resultado
print(a.mean()) # faz a media do resultado dos numeros
print(a[a > 5]) # imprime todos os numeros maiores que 5
print(a[a % 3 == 0]) # imprime os numeros multiplos de 3
'''

a = np.array([7.5, 6.0, 8.5 , 7.0])

#letra A
#print(a.mean()) # faz a media do resultado dos numeros

#letra B
#print(a.max(),"maior nota") 
#print(a.min(),"menor nota") 

#letra C
#print(a[a > 7.2]) # imprime todos os numeros maiores que 5

#letra D
#notas_arredondadas = np.round(a)
#print(notas_arredondadas)

a = np.array([19.90, 35.50, 42.00, 8.90, 120.00, 55.00])

#letra B
#print(a-a*0.15) 

#letra C
#desconto = 0.15  # 15%
#precos_com_desconto = a * (1 - desconto)
#resultado = precos_com_desconto[precos_com_desconto > 30]
#print(resultado)

#letra D
desconto = 0.15  # 15%
precos_com_desconto = a * (1 - desconto)
total = precos_com_desconto.sum()
print(total)
