from src.pessoa import Pessoa
from src.acoes.falar import IniciarFala
from src.acoes.estudar import IniciarEstudos

pessoa1 = Pessoa(IniciarFala())
pessoa1.realiza_acao()

pessoa2 = Pessoa(IniciarEstudos())
pessoa2.realiza_acao()
