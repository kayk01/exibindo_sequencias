# Inicializa a variável de incremento
incremento = 25

# Loop para gerar a sequência
for i in range(0, 201, incremento):
    print(i, end=", ")

# Inicializa o primeiro número da sequência
numero = 200


# Loop para gerar a sequência decrescente
while numero > 25:
    print(numero, end=", ")
    numero //= 2


# Imprime o último número da sequência (25)
print(numero)
