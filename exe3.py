import pandas as pd
import numpy as np

# Lendo o arquivo JSON com Pandas
df = pd.read_json('dados.json')

# Convertendo os valores em array
faturamentos_array = df['valor'].values

#declarando as variaveis que vamos utilizar
menorValor = faturamentos_array[0]
maiorValor = faturamentos_array[0]
media = 0
contador = 0

#roda o vetor verificando maior e menor valor e somando os valores na media desconsiderando 0
for valor in faturamentos_array:
    if(valor > maiorValor and valor != 0):
        maiorValor = valor
    if(valor < menorValor and valor != 0):
        menorValor = valor

    if(valor != 0): 
        media += valor
        contador += 1
    
#calculando media geral
media = media/contador

#verificando quantos dias foram acima da media
acimaMedia = 0

for valor in faturamentos_array:
    if(valor > media):
        acimaMedia +=1

#printando os resultados
print(f'o maior valor foi {maiorValor}')
print(f'o menor valor foi {menorValor}')
print(f'a media geral foi de {media} tiveram {acimaMedia} valores acima da media mensal')
