#importação
from collections import defaultdict

#criação de um default dict com uma lista como valor padrão
dicionario_lista = defaultdict(list)
dicionario_lista["PRODUTO"] = "Macbook Pro"
dicionario_lista["MARCA"] = "Apple"

print(dicionario_lista["PREÇO"])
print(dicionario_lista)

#criação de função que retorna a frase "INEXISTENTE"
def funcao_exemplo():
    return "INEXISTENTE"
dicionario_funcao = defaultdict(funcao_exemplo)
dicionario_funcao["PRODUTO"] = "Macbook Pro"
dicionario_funcao["MARCA"] = "Apple"

print(dicionario_funcao)
print(dicionario_funcao["PREÇO"])
print(dicionario_funcao)

#criação de dicionario com uma função lambda
dicionario_lambda = defaultdict(lambda: "Não disponível")
dicionario_lambda["PRODUTO"] = "Macbook Pro"
dicionario_lambda["MARCA"] = "Apple"

print(dicionario_lambda)
print(dicionario_lambda["PREÇO"])
print(dicionario_lambda)