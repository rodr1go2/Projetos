def calcular_media(notas):
    if not notas:
        return 0 
    total = sum(notas)
    media = total / len(notas)
    return media

lista_de_notas = []
quantidade_notas = int(input('Quantas notas você deseja inserir? '))

for i in range(quantidade_notas):
    nota  = float(input(f'Digite sua a {i+1}ª nota:  '))
    lista_de_notas.append(nota)

media_final = calcular_media(lista_de_notas)

print('----RESULTADO----')
print(f'Notas informadas: {lista_de_notas}')
print(f'A media final do aluno é: {media_final:.2f}')

if media_final >= 6.0:
    print('Aprovado')
else:
    print('REPROVADO')
    