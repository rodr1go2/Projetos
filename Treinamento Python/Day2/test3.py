def contar_vogais(texto):
    vogais = 'aeiou'
    contador = 0
    texto = texto.lower()
    for caractere in texto:
        if caractere in vogais:
            contador += 1
    return contador

texto_exemplo = 'Ola, Mundo!'
print(f'A frase {texto_exemplo} tem {contar_vogais(texto_exemplo)} vogais.')