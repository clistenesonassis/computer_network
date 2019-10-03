class Pacote:

    def __init__(self, origem, destino, dados):
        self.origem = origem
        self.destino = destino
        self.dados = dados
        self.tamanhodados = len(dados)
        self.quantDados = dados.split()
        self.protocol = ""

    def setOrigem(self, num1, num2):
        self.origem = str(num1) + '.' + str(num2)

    def setDestino(self, num1, num2):
        self.destino = str(num1) + '.' + str(num2)

    def setProtocol(self, protocol):
        self.protocol = protocol
