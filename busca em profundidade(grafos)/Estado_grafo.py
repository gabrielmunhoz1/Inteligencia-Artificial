class Estado:
    def __init__(self, posicao):
        if posicao == None:
            self.posicao = self.getEstadoInicial()

        else:
            self.posicao = posicao

    def getEstadoInicial(self):
        estadoInicial = self.Grafo[0][0]
        return estadoInicial
    
    #retorna uma lista com os indices dos próximos vértices que podem ser visitados
    def funcaoSucessora(self):
        lista = []
        for i in range(len(self.posicao)):
            if self.posicao[i] == 1:
                lista.append(i)
        return lista

    #se a posição for o indice 6, ou seja, se estiver no ultimo vértice(ultima lista) do Grafo quer dizer que chegou no objetivo
    def funcaoObjetivo(self):
        if self.posicao == 6:
            return True
        else:
            return False