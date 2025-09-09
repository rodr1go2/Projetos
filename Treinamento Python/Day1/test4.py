vogais = 'aáàâãeéêiíouúû'

texto = input('Digite um texto: ').lower()
contador_vogais = 0 

for caractere in texto:
    if caractere in vogais:
        contador_vogais += 1

print(f'O texto informado possui {contador_vogais} vogais.')
   