Origem_carga = int (input("Digite qual o estado de origem (1 a 5): "))
Peso_caminhao = float(input("Digite qual o peso do caminhão em toneladas: "))
Codigo_carga = int(input("Digite qual o codigo da carga(10 a 40): "))

peso_Kilos = Peso_caminhao * 1000
 
if Codigo_carga >= 10 and Codigo_carga <= 20:
    preco_kilo = 100.00
elif Codigo_carga >= 21 and Codigo_carga <= 30:
    preco_kilo = 250.00
elif Codigo_carga >= 31 and Codigo_carga <= 40:
    preco_kilo = 340.00

preco_total = preco_kilo * peso_Kilos

match Origem_carga:
    case 1:
        taxa_imposto = 0.35
    case 2:
        taxa_imposto = 0.25
    case 3:
       taxa_imposto = 0.15
    case 4:
        taxa_imposto = 0.05
    case 5:
        taxa_imposto = 0

imposto = preco_total * taxa_imposto

ValorTotal = preco_total + imposto

print("==============================")
print("===== Resumo do Cálculo  =====")
print("==============================")
print(f"A conversão em Kilos é:{peso_Kilos:,.2f}kg")
print(f"O preço da carga é: {preco_total:,.2f}R$")
print(f"O valor do imposto é: {imposto:,.2f}R$")
print(f"O valor total é de {ValorTotal:,.2f}R$")
print("==============================")
