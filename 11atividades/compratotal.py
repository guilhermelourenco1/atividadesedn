produto = "Whisky Single Malt"
preco_unitario = 239.90
quantidade_comprada = 3
valor_total = preco_unitario * quantidade_comprada

comprovante = f"""
+--------------------- RECIBO DE COMPRA ---------------------+
|                                                            |
| Produto: {produto:<39}           |
| Preço unitário: R$ {preco_unitario:>10.2f}                              |
| Quantidade adquirida: {quantidade_comprada:<10}                           |
|                                                            |
| ---------------------------------------------------------- |
| VALOR TOTAL: R$ {valor_total:>16.2f}                           |
|                                                            |
|           MUITO OBRIGADO PELA SUA CONFIANÇA!               |
|              VOLTE SEMPRE PARA MAIS EXPERIÊNCIAS           |
|____________________________________________________________|
"""

print(comprovante)