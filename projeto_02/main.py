import os

from models.endereco import Endereco
from models.enums.estado import Estado
from models.enums.sexo import Sexo
from models.pessoa import Pessoa

def limpa():
    os.system("cls || clear")


pessoa_01 = Pessoa(2514,"João", 19, "7199999-9999", "joao@gmail.com", Sexo.MASCULINO, Endereco("Rua A", "55", "proximo a  lagoa", "55.900-000", "Xique-xique", Estado.BAHIA))


# limpa()
print(pessoa_01)