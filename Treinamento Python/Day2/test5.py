vendas = [
    {'produto': 'camisa', 'valor':50.00, 'quantidade':2 },
    {"produto": "calça", "valor": 80.00, "quantidade": 1},
    {"produto": "camisa", "valor": 50.00, "quantidade": 3},
    {"produto": "sapato", "valor": 120.00, "quantidade": 1},
    {"produto": "calça", "valor": 80.00, "quantidade": 2}
]

vendas_por_produto = {}
quantidades_por_produto = {}

for venda in vendas:
    produto = venda['produto']
    valor_total = venda['valor'] * venda['quantidade']

    vendas_por_produto[produto] = quantidades_por_produto.get(produto, 0) + valor_total
    quantidades_por_produto[produto] = quantidades_por_produto.get(produto, 0) + venda["quantidade"]

print("Valor total de vendas por produto:")
for produto, valor in vendas_por_produto.items():
     print(f"- {produto}: R${valor:.2f}")

produto_mais_vendido = max(quantidades_por_produto, key=quantidades_por_produto.get)
print(f"\nO produto mais vendido em quantidade é: '{produto_mais_vendido}'")