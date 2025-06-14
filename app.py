
def quanto_precisa(i):
    if i >= qtd_grupos:
        return 0
    
    if i == 0:
        return grupos_ml[i] + quanto_precisa(i + 1)
    
    return (grupos_ml[i] + quanto_precisa(i + 1)) / 2

qtd_grupos = int(input("Quantos grupos?"))
peso_animais, grupos_ml = [], []

for i in range(qtd_grupos):
    peso = int(input(f"Grupo {i + 1}: "))
    peso_animais.append(peso)
    grupos_ml.append(peso / 100)

print(peso_animais)
print(grupos_ml)
print(quanto_precisa(0))
