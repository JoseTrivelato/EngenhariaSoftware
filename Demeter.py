class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def imprimir_produtos_comprados(self):
        for pedido in self.pedidos:
            for item in pedido.itens:
                print(f"Cliente {self.nome} comprou: {item.produto}")

class Pedido:
    def __init__(self, numero):
        self.numero = numero
        self.itens = []

    def adicionar_item(self, produto):
        self.itens.append(ItemPedido(produto))

class ItemPedido:
    def __init__(self, produto):
        self.produto = produto


cliente1 = Cliente("João")
pedido1 = Pedido(1)
pedido1.adicionar_item("Camiseta")
pedido1.adicionar_item("Calça")
cliente1.adicionar_pedido(pedido1)

pedido2 = Pedido(2)
pedido2.adicionar_item("Tênis")
cliente1.adicionar_pedido(pedido2)

cliente1.imprimir_produtos_comprados()
