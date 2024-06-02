maior_idade = True
possui_carteira_trabalho = True
possui_veiculo_proprio = False
print(maior_idade and possui_carteira_trabalho)
print(possui_carteira_trabalho or possui_carteira_trabalho)

#Desafio
possui_passaporte = False
passagem_comprada = False
menor_de_idade = False
print((possui_passaporte and passagem_comprada) and (not menor_de_idade))
print((possui_passaporte or passagem_comprada) and (not menor_de_idade))
print(( not possui_passaporte or passagem_comprada) and (not menor_de_idade))
print(( not possui_passaporte or not passagem_comprada) and (menor_de_idade))
