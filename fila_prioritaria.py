class FilaPrioritaria:
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'PR{self.codigo}'

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente Atual: {cliente_atual}, dirija-se ao caixa {caixa}'

    def estatistica(self, dia: str, age: int, flag: str) -> dict:
        if flag != 'detail':
            estatistica = {f'{age}-{dia}': len(self.clientes_atendidos)}
        else:
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = age
            estatistica['Clientes Atendidos'] = self.clientes_atendidos
            estatistica['Qtde Clientes Atendidos'] = len(self.clientes_atendidos)

        return estatistica


