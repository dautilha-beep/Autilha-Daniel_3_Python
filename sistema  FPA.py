
# SISTEMA DE FATURACAO DE UMA LOJA DE PRODUTOS ALIMENTARES

fila_prioritaria = []
fila_normal = []

quantidade = int(input("Quantos clientes deseja registar? "))

for i in range(quantidade):

    print("\n--- REGISTO DO CLIENTE", i + 1, "---")

    nome = input("Nome do cliente: ")
    genero = input("Genero (M/F): ").upper()
    idade = int(input("Idade do cliente: "))
    compras = float(input("Valor total das compras (Kz): "))

    # Calculo do bonus de 10%
    if compras > 100000:
        bonus = compras * 0.10
    else:
        bonus = 0

    # Calculo do valor final
    total_pagar = compras - bonus

    # Verificacao das condicoes de prioridade
    gravida = input("A cliente esta gravida? (S/N): ").upper()
    deficiencia = input("O cliente tem deficiencia? (S/N): ").upper()

    if (idade >= 60 or deficiencia == "S"
            or (genero == "F" and gravida == "S")):

        prioridade = "SIM"
        fila_prioritaria.append(nome)

    else:
        prioridade = "NAO"
        fila_normal.append(nome)

    # Emissao da factura
    print("\n========== FACTURA ==========")
    print("Nome do cliente:", nome)
    print("Valor das compras:", compras, "Kz")
    print("Bonus atribuido:", bonus, "Kz")
    print("Total a pagar:", total_pagar, "Kz")
    print("Tem prioridade:", prioridade)
    print("=============================")

# Apresentacao das filas
print("\n========== FILA DE ATENDIMENTO ==========")

print("\nCLIENTES PRIORITARIOS:")
if len(fila_prioritaria) > 0:
    for cliente in fila_prioritaria:
        print("-", cliente)
else:
    print("Nao existem clientes prioritarios.")

print("\nCLIENTES DA FILA NORMAL:")
if len(fila_normal) > 0:
    for cliente in fila_normal:
        print("-", cliente)
else:
    print("Nao existem clientes na fila normal.")

print("\nFim do programa!")
