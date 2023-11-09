nome = "texto.txt"

arq = open(nome, "r", encoding="utf-8")

conteudo = arq.read()
conteudo = conteudo.lower()

vogais = "aeiouAEIOU"
cont_vogais = 0

for letra in conteudo:
    if letra in vogais:
        cont_vogais += 1

print(f"O número de vogais no texto é: {cont_vogais}")

arq.close()
