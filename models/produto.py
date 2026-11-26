class Produto:
    def __init__(self, nome, preco, estoque, categoria, fornecedor):
        self.nome = nome
        self.preco = float(preco)
        self.estoque = int(estoque)
        self.categoria = categoria
        self.fornecedor = fornecedor

    def apresentar(self):
        return (
            f"Produto: {self.nome}\n"
            f"Preço: R$ {self.preco:.2f}\n"
            f"Estoque: {self.estoque}\n"
            f"Categoria: {self.categoria.nome}\n"
            f"Fornecedor: {self.fornecedor.nome}\n"
        )

    def calcular_valor_estoque(self):
        return self.estoque * self.preco

    def adicionar_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        self.estoque += quantidade
        print(f"Adicionado {quantidade}. Atual: {self.estoque}")

    def remover_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if self.estoque < quantidade:
            raise ValueError(f"Estoque insuficiente. Atual: {self.estoque}")
        self.estoque -= quantidade
        print(f"Removido {quantidade}. Atual: {self.estoque}")