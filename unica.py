class Calculadora:
    def somar(self, x, y):
        return x + y

    def subtrair(self, x, y):
        return x - y

    def multiplicar(self, x, y):
        return x * y

    def dividir(self, x, y):
        if y == 0:
            raise ValueError("Não é possível dividir por zero.")
        return x / y

# Exemplo de uso
calculadora = Calculadora()
print("Soma:", calculadora.somar(5, 3))
print("Subtração:", calculadora.subtrair(8, 2))
print("Multiplicação:", calculadora.multiplicar(4, 6))
print("Divisão:", calculadora.dividir(10, 2))
