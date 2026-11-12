from models.produto import Produto

def calcular_valor_total(produtos: list[Produto]) -> float:
    """Calcula o valor total em estoque de uma lista de produtos.
    Args:
        produtos (list[Produto]): Lista de produtos.
    Returns:
        float: Valor total em estoque.
    """
    total = 0.0
    for produto in produtos:
        total += produto.calcular_valor_total()
    return total


def listar_produtos_estoque_baixo(produtos: list[Produto], limite: int) -> list[Produto]:
    """Lista produtos cuja quantidade em estoque seja menor ou igual ao limite
    Args:
        produtos (list[Produto]): Lista de produtos.
        limite (int): Limite de estoque.
    Returns:
        list[Produto]: Lista de produtos com estoque abaixo do limite.
    """
    produtos_baixo_estoque = []
    for produto in produtos:
        if produto.quantidade <= limite:
            produtos_baixo_estoque.append(produto)
    return produtos_baixo_estoque


def ordenar_produtos_por_valor_total(produtos: list[Produto]) -> list[Produto]:
    """Ordena os produtos por valor total em estoque.
    Args:
        produtos (list[Produto]): Lista de produtos.
    Returns:
        list[Produto]: Lista de produtos ordenada por valor total.
    """
    return sorted(produtos, key=lambda produto: produto.calcular_valor_total(), reverse=True)


def buscar_produto_por_nome(produtos: list[Produto], nome: str) -> Produto | None:
    """Busca um produto pelo nome.
    Args:
        produtos (list[Produto]): Lista de produtos.
        nome (str): Nome do produto a ser buscado.
    Returns:
        Produto | None: Produto encontrado ou None se não encontrado.
    """
    for produto in produtos:
        if produto.nome == nome:
            return produto
    return None

