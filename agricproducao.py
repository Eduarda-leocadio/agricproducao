cultura1 = "Alface"
cultura2 = "Cenoura"
cultura3 = "Tomate"
cultura4 = "Batata"
cultura5 = "Milho"

gasto1 = {"arrendamento": 500.0, "maodeobra": 3000.0, "mudas": 50000.0, "energia": 600.0, "insumos": 2500.0}
venda1 = {"valor_unidade": 4.00, "quantidade": 50000.0}
lucrobruto1 = venda1["valor_unidade"] * venda1["quantidade"]
custo1 = gasto1["arrendamento"] + gasto1["maodeobra"] + gasto1["energia"] + gasto1["insumos"]
lucroliquido1 = lucrobruto1 - custo1

gasto2 = {"arrendamento": 600.0, "maodeobra": 2500.0, "mudas": 60000.0, "energia": 600.0, "insumos": 2500.0}
venda2 = {"valor_unidade": 1.50, "quantidade": 20000.0}
lucrobruto2 = venda2["valor_unidade"] * venda2["quantidade"]
custo2 = gasto2["arrendamento"] + gasto2["maodeobra"] + gasto2["energia"] + gasto2["insumos"]
lucroliquido2 = lucrobruto2 - custo2

gasto3 = {"arrendamento": 750.0, "maodeobra": 4000.0, "mudas": 70000.0, "energia": 650.0, "insumos": 3000.0}
venda3 = {"valor_unidade": 1.50, "quantidade": 15000.0}
lucrobruto3 = venda3["valor_unidade"] * venda3["quantidade"]
custo3 = gasto3["arrendamento"] + gasto3["maodeobra"] + gasto3["energia"] + gasto3["insumos"]
lucroliquido3 = lucrobruto3 - custo3

gasto4 = {"arrendamento": 500.0, "maodeobra": 300.0, "mudas": 80000.0, "energia": 600.0, "insumos": 3000.0}
venda4 = {"valor_unidade": 2.00, "quantidade": 160000.0}
lucrobruto4 = venda4["valor_unidade"] * venda4["quantidade"]
custo4 = gasto4["arrendamento"] + gasto4["maodeobra"] + gasto4["energia"] + gasto4["insumos"]
lucroliquido4 = lucrobruto4 - custo4

gasto5 = {"arrendamento": 500.0, "maodeobra": 200.0, "mudas": 100000.0, "energia": 1000.0, "insumos": 4000.0}
venda5 = {"valor_espiga": 1.00, "quantidade": 200000.0}
lucrobruto5 = venda5["valor_espiga"] * venda5["quantidade"]
custo5 = gasto5["arrendamento"] + gasto5["maodeobra"] + gasto5["energia"] + gasto5["insumos"]
lucroliquido5 = lucrobruto5 - custo5


menu = f"Bem-vindo ao sistema de produção agrícola! Agricprodução \n" \
         f"1. {cultura1}\n" \
         f"2. {cultura2}\n" \
         f"3. {cultura3}\n" \
         f"4. {cultura4}\n" \
         f"5. {cultura5}\n"
print(menu)
escolha = input("Escolha uma cultura : ")
hectares = float(input("Informe a área em hectares: "))

gasto1 = {k: v * hectares for k, v in gasto1.items()}
gasto2 = {k: v * hectares for k, v in gasto2.items()}
gasto3 = {k: v * hectares for k, v in gasto3.items()}
gasto4 = {k: v * hectares for k, v in gasto4.items()}  
gasto5 = {k: v * hectares for k, v in gasto5.items()}

if escolha == "1":
    print(f"Cultura selecionada: {cultura1}")
    print("Custos:")
    for gasto, valor in gasto1.items():
        if gasto in ["arrendamento", "maodeobra", "energia", "insumos"]:
            print(f"{gasto}: R$ {valor:.2f}")
    print(f"Lucro Bruto: R$ {lucrobruto1:.2f}")
    print(f"Lucro Líquido: R$ {lucroliquido1:.2f}")

elif escolha == "2":
    print(f"Cultura selecionada: {cultura2}")
    print("Gastos:")
    for gasto, valor in gasto2.items():
        if gasto in ["arrendamento", "maodeobra", "energia", "insumos"]:
            print(f"{gasto}: R$ {valor:.2f}")
    print(f"Lucro Bruto: R$ {lucrobruto2:.2f}")
    print(f"Lucro Líquido: R$ {lucroliquido2:.2f}")

elif escolha == "3":
    print(f"Cultura selecionada: {cultura3}")
    print("Gastos:")
    for gasto, valor in gasto3.items():
        if gasto in ["arrendamento", "maodeobra", "energia", "insumos"]:
            print(f"{gasto}: R$ {valor:.2f}")
    print(f"Lucro Bruto: R$ {lucrobruto3:.2f}")
    print(f"Lucro Líquido: R$ {lucroliquido3:.2f}")

elif escolha == "4":
    print(f"Cultura selecionada: {cultura4}")
    print("Gastos:")
    for gasto, valor in gasto4.items():
        if gasto in ["arrendamento", "maodeobra", "energia", "insumos"]:
            print(f"{gasto}: R$ {valor:.2f}")
    print(f"Lucro Bruto: R$ {lucrobruto4:.2f}")
    print(f"Lucro Líquido: R$ {lucroliquido4:.2f}")

elif escolha == "5":
    print(f"Cultura selecionada: {cultura5}")
    print("Gastos:")
    for gasto, valor in gasto5.items():
        if gasto in ["arrendamento", "maodeobra", "energia", "insumos"]:
            print(f"{gasto}: R$ {valor:.2f}")
    print(f"Lucro Bruto: R$ {lucrobruto5:.2f}")
    print(f"Lucro Líquido: R$ {lucroliquido5:.2f}")

else:
    print(ValueError("Opção inválida! Por favor, escolha uma cultura válida."))

print("\nObrigado por usar o sistema de produção agrícola!")
print("\nFim do programa.")