print("QUESTÃO IMPOSTO DE RENDA")

def calcular_imposto(salario):
    if salario <= 2000.00:
        return "Isento"
    elif salario > 2000.00 and salario <= 3000.00:
        return (salario - 2000.00) * 0.08 
    elif salario > 3000.00 and salario <= 4500.00:
        return (salario - 3000.00) * 0.18  
    elif salario > 4500.00 :
        return (salario - 4500.00) * 0.28  
    
# Solicita o valor do salário ao usuário
salario = float(input("Digite o seu salário: R$ "))

# Calcula o imposto
imposto = calcular_imposto(salario)

# Exibe o imposto formatado para duas casas decimais
print(f"O imposto a ser pago é: R$ {imposto}")