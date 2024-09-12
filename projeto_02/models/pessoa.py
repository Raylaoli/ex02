from models.endereco import Endereco
from models.enums.sexo import Sexo


class Pessoa:
    def __init__(self, id: int, nome: str, idade: int, telefone: str, email: str, sexo: Sexo, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.endereco = endereco