def quanto_precisa(i):
    if i >= qtd_grupos:
        return 0
    
    resultado = grupos_ml[i] + quanto_precisa(i + 1)

    if i == 0:
        return resultado
    
    print(f"Grupo {i + 1}: {resultado / 2} mL de água")

    return resultado / 2

qtd_grupos = int(input("Quantos grupos?"))
peso_animais, grupos_ml = [], []

for i in range(qtd_grupos):
    peso = int(input(f"Grupo {i + 1}: "))
    peso_animais.append(peso)
    grupos_ml.append(peso / 100)

print(peso_animais)
print(grupos_ml)

ml_primeiro = quanto_precisa(0)

print(f"Grupo Mãe inicialmente: {ml_primeiro} mL de 25mg / kg")
print(f"mg de medicamento: {(ml_primeiro / 10 * 25):.4f} mg")