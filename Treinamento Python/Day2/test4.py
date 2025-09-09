import re

def eh_palindromo(frase):
    frase_limpa = re.sub(r'[^a-zA-Z]', '', frase).lower()
    return frase_limpa == frase_limpa[::-1]

print(f"A frase 'A sacada da casa' é um palíndromo? {eh_palindromo('A sacada da casa')}")
print(f"A palavra 'python' é um palíndromo? {eh_palindromo('python')}")