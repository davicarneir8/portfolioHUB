def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Conversor de Temperatura")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")
opcao = input("Escolha uma opção (1 ou 2): ")

if opcao == "1":
    c = float(input("Digite a temperatura em Celsius: "))
    f = celsius_para_fahrenheit(c)
    print(f"{c}°C é igual a {f:.2f}°F")
elif opcao == "2":
    f = float(input("Digite a temperatura em Fahrenheit: "))
    c = fahrenheit_para_celsius(f)
    print(f"{f}°F é igual a {c:.2f}°C")
else:
    print("Opção inválida.")