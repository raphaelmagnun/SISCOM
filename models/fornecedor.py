class Fornecedor:
    def __init__(self, nome, telefone="", email=""):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def apresentar(self):
        return (
            f"Fornecedor: {self.nome}\n"
            f"Telefone: {self.telefone}\n"
            f"E-mail: {self.email}\n"
        )