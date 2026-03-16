rato = "o rato roeu a roupa do rei de roma"

contagem = {}

for palavra in rato.split():
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(contagem)