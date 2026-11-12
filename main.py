from models.produto import Produto
from services.estoque import calcular_valor_total, listar_produtos_estoque_baixo, ordenar_produtos_por_valor_total, buscar_produto_por_nome

produto1 = Produto("Produto A", 10.0, 5)
produto2 = Produto("Produto B", 200.0, 10)
produto3 = Produto("Produto C", 60, 4)

produto1.atualizar_preco(12.0)
produto2.adicionar_estoque(2)
produto3.remover_estoque(1)

produto1.exibir_informacoes()
produto2.exibir_informacoes()
produto3.exibir_informacoes()

produtos = [produto1, produto2, produto3]

print(f"Valor total em estoque: {calcular_valor_total(produtos)}")
print(f"Produtos com estoque abaixo de 5 unidades: {[f'{produto.nome} - {produto.quantidade}' for produto in listar_produtos_estoque_baixo(produtos, 5)]}")
print(f"Produtos ordenados por valor total: {[f'{produto.nome} - {produto.calcular_valor_total()}' for produto in ordenar_produtos_por_valor_total(produtos)]}")
print()
print(f"Produto buscado por nome 'Produto B': {buscar_produto_por_nome(produtos, 'Produto B')}")
print(f"Produto buscado por nome 'Produto D': {buscar_produto_por_nome(produtos, 'Produto D')}")