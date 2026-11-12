from models.produto import Produto
from services.estoque import calcular_valor_total, listar_produtos_estoque_baixo, ordenar_produtos_por_valor_total, buscar_produto_por_nome

produto1 = Produto("Produto A", 10.0, 5)
