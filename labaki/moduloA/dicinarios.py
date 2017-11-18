#  dicionarios

aurelio = {'denominação': 'ilha solteira', 'população': 23000, 'renda': 1500}
print(aurelio)
print(aurelio.keys())  # mostra somente as chaves contidas no dicionario
aurelio['vocação'] = 'turismo'  # inseri uma nova chave (vocação) ao dicionario e atribui o valor (turismo) a ela
print(aurelio.keys())
print(aurelio['renda'])  # mostra o valor contido na chave (renda).
aurelio['renda'] = aurelio['renda'] + 200  # soma 200 ao valor contido na chave (renda)
print(aurelio['renda'])
print('idade' in aurelio)  # verifica se existe a chave (idade) no dicionario
aurelio['idade'] = 33  # inseri a chave (idade) e atribui o valor (33) a ela
print('idade' in aurelio)
print(aurelio.items())