import os

from models.endereco import Endereco
from models.enums.sexo import Sexo
from models.pessoa import Pessoa
from models.enums.estado import Estado

os.system("cls || clear")


pessoa_01 = Pessoa(2514,"João", 19, "7199999-9999", "joao@gmail.com", Sexo.MASCULINO, Endereco("Rua A", "55", "proximo a  lagoa", "55.900-000", "Xique-xique", Estado.BAHIA))


print(pessoa_01)