#declarando os valores por estado
faturamento_mensal = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}

#somando todos valores pra fazer porcentagem
soma_total = 0
for valor in faturamento_mensal.values():
    soma_total += valor
print(soma_total)

#calculando porcentagens
for estado in faturamento_mensal:
    faturamento_mensal[estado] = (faturamento_mensal[estado]*100)/soma_total
    print(f'a porcentagem de contribuição de {estado} é igual a {faturamento_mensal[estado]}')