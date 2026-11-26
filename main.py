from models import Categoria, Produto, Fornecedor, MovimentoEstoque

#Criando categorias
categoria1 = Categoria("Eletrônicos", "Produtos eletrônicos e gadgets")
categoria2 = Categoria("Papelaria", "Materiais Escolares")
categoria3 = Categoria("Informática", "Acessórios e equipamentos")

#Cadastrando fornecedores
fornecedor1 = Fornecedor("Fornecedor A", "Rua A, 123", "(11) 1234-5678")
fornecedor2 = Fornecedor("Fornecedor B", "Rua B, 456", "(11) 9876-5432")

#Cadastrando produtos
produto1 = Produto("Notebook", 10, 5000.00, categoria1, fornecedor1)
produto2 = Produto("Caneta", 100, 2.50, categoria2, fornecedor2)
produto3 = Produto("Teclado", 20, 150.00, categoria3, fornecedor1)

#Exibindo informações dos produtos
print(produto1.apresentar())
print(produto2.apresentar())
print(produto3.apresentar())

#Movimentos de estoque
movimento1 = MovimentoEstoque("entrada", 5, "2024-06-01", produto1)
movimento2 = MovimentoEstoque("saida", 10, "2024-06-02", produto2)

#Executando movimentos de estoque
try:
    movimento1.executar()
    movimento2.executar()
except Exception as e:
    print(f"Erro ao executar movimento de estoque: {e}")

#Exibindo informações dos produtos após os movimentos de estoque
print(produto1.apresentar())
print(produto2.apresentar())
print(produto3.apresentar())