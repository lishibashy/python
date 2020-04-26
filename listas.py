import random

#Uso da função random com listas
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']

escolhida = random.choice(cidades)

print('A cidade escolhida foi: ', escolhida)


#Uso da função append
a = [1, 2, 3]

a.append(15)

print(a)


#Uso da função append com arrays
b = [7, 8, 9]

for item in b:
    a.append(item)
print(a)