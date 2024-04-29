from abc import ABC, abstractmethod

class Produto(ABC):
    @abstractmethod
    def calcular_preco(self):
        pass

class ProdutoSimples(Produto):
    def __init__(self, preco):
        self.preco = preco

    def calcular_preco(self):
        return self.preco

class ProdutoComDesconto(Produto):
    def __init__(self, produto, desconto):
        self.produto = produto
        self.desconto = desconto

    def calcular_preco(self):
        return self.produto.calcular_preco() * (1 - self.desconto)

class Pedido:
    def __init__(self, produtos):
        self.produtos = produtos

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.calcular_preco()
        return total

# Exemplo de uso
produto1 = ProdutoSimples(50)
produto2 = ProdutoComDesconto(ProdutoSimples(30), 0.1)  # Produto com desconto de 10%

pedido = Pedido([produto1, produto2])
print("Total do pedido:", pedido.calcular_total())
