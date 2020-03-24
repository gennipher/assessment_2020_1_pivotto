salario_bruto = float(input("Salário Bruto: R$ "))
parcela_mensal = float(input("Quanto será a parcela paga por mês? R$ "))
porcentagem = salario_bruto * (30/100)

porcentagem_comprometida = int(((parcela_mensal/salario_bruto) * 100))

# Resposta se o empréstimo pode ser concedido ou não:
if (parcela_mensal <= porcentagem):
    print("\nO empréstimo pode ser concedido.")
else:
    print("\nO empréstimo não pode ser concedido.")

# Mostrar salário bruto do trabalhador
print("\n--------------------------------------------------------------------------")
print(f"\nSalário Bruto: R$ {salario_bruto}")

# Mostrar a parcela mensal do empréstimo:
print(f"Parcela Mensal do empréstimo: R$ {parcela_mensal}")

# Mostrar qual a porcentagem que a parcela compromete do salário bruto:
print(f"Porcentagem que a parcela compromete do Salário Bruto: {porcentagem_comprometida}%")