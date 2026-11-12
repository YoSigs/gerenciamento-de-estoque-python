class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int) -> None:
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_total(self) -> float:
        return self.preco * self.quantidade

    def exibir_informacoes(self) -> None:
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Valor total: {self.calcular_valor_total()}")

    def atualizar_preco(self, novo_preco: float) -> None:
            self.preco = novo_preco

    def atualizar_quantidade(self, nova_quantidade: int) -> None:
            self.quantidade = nova_quantidade

    def adicionar_estoque(self, quantidade_adicional: int) -> None:
        if quantidade_adicional < 0:
            print("Valor inválido. Digite um número positivo.")
        else:
            self.quantidade += quantidade_adicional

    def remover_estoque(self, quantidade_removida: int) -> None:
        if quantidade_removida <= 0:
            print("Valor inválido. Digite um número positivo.")
        elif quantidade_removida <= self.quantidade:
            self.quantidade -= quantidade_removida
        else:
            print("Quantidade a remover é maior que a quantidade em estoque.")

    @property
    def quantidade(self) -> int:
        return self._quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade: int) -> None:
        if nova_quantidade < 0:
            print("Valor inválido. Digite um número positivo.")
        else:
            self._quantidade = nova_quantidade

    @property
    def preco(self) -> float:
        return self._preco

    @preco.setter
    def preco(self, novo_preco: float) -> None:
        if novo_preco < 0:
            print("Valor inválido. Digite um número positivo.")
        else:
            self._preco = novo_preco