#criação do dicionário
dicionario = {
    "Nome":"Star Wars",
    "Diretor":"George Lucas",
    "Ano de lançamento":1977,
    "bilheteria": 775000000.00
}

#exibição do dicionário completo
print(dicionario)

#exibição do valor de uma chave
print(dicionario["Nome"])

#inserção de uma nova chave e valor (gênero)
dicionario["Gênero"] = "Space Opera"
print(dicionario)

#método keys
print(dicionario.keys())
for chave in dicionario.keys():
    print(chave)

#método values
print(dicionario.values())
for valor in dicionario.values():
    print(valor)

#metodo itens
print(dicionario.items())
for chave, valor in dicionario.items():
    print(f"{chave} -- {valor}")

#método get
print(dicionario.get("público"))
print(dicionario.get("Nome"))

#método setdefault
dicionario.setdefault("público", 1000)
print(dicionario)
dicionario.setdefault("público", 9000)
print(dicionario)