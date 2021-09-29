from Estado_grafo import Estado

class No():
    
    def __init__(self, estado):
        self.estado = Estado.posicao
        self.profundidade = 0
        self.filhos = []
        self.pai = None
    
    def addFilho(self, noFilho):
        self.filhos.append(noFilho)
        noFilho.pai = self
        noFilho.profundidade = self.profundidade + 1

    def printArvore(self):
        print(self.profundidade, '-', self.estado.posicao)
        for umFilho in self.filhos:
            umFilho.printArvore()

    def printCaminho(self):
        if self.pai != None:
            self.pai.printCaminho()
        print("-> ", self.estado.nome)



