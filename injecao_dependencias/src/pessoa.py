class Pessoa:
    def __init__(self, comportamento) -> None:

        self.comportamento = comportamento

    def realiza_acao(self):
        self.comportamento.acao()
