# Calculadora de Consumo Elétrico Inteligente
# Autor: Inês Martinelli
# Entrada
aparelho = input("Insira o nome do aparelho elétrico utilizado: ")
potencia = int(input("Insira a potência do aparelho em watts (W): "))
horasDia = float(input("Insira o tempo médio de uso diário em horas (h): "))
# Processamento: 
# 1) Cálculo do consumo mensal (estimado) em kWh/mês;
# 2) Cálculo do custo mensal estimado em kWh, dado pelo consumo mensal multiplicado pelo valor fixo de 0.65 centavos de Real (R$).
consumoMensal = (potencia * horasDia * 30) / 1000
gastomensal = (consumoMensal * 0.35)
# Saída
print("====================================================================")
print("Aparelho:",aparelho)
print("Consumo estimado:",consumoMensal, "kWh/mês")
print(f"Gasto mensal estimado: R$ {gastomensal:.2f} por kWh")

