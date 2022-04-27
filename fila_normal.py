class FilaNormal:
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""

    def GeraSenhaAtual(self) -> None:
        self.senha_atual = f'NM{self.codigo}'

    def ResetaFila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def AtualizaFila(self) -> None:
        self.ResetaFila()
        self.GeraSenhaAtual()
        self.fila.append(self.senha_atual)

    def ChamaCliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente Atual: {cliente_atual}, dirija-se ao caixa {caixa}'
