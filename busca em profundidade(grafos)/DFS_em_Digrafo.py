class grafo_direcionado():
    def __init__(self, V):
        self.V = V #número de vértices
        self.E = 0 #número de arestas
        self.adj = [[] for _ in range(V)] #lista de adjacencias
    
    def insere(self, v, w):
        if w not in self.adj[v]: # se o item w não estiver em v, adiciona w na lista v 
            self.adj[v-1].append(w-1) #adiciona (na lista de adjacencias) na lista v o item w
            self.E += 1 #adiciona + 1 na contagem das arestas

#-----Busca em Profundidade------
tempo = -1

def DFS(g):
    visitado = [False] * g.V # lista de vértices visitados (True) e não visitados (False)
    d = [-1] * g.V #lista de tempo que cada vértice foi descoberto  
    f = [-1] * g.V #lista de tempo que cada vértice foi examinado por completo 
    pai = [-1] * g.V 
    for u in range(g.V):
        if not visitado[u]:
            pai[u] = u
            DFS_visita(g, u, pai, d, f, visitado)
    
    print('pai: {}'.format(pai))
    print('d:   {}'.format(d))
    print('f:   {}'.format(f))
    print('Adj: {}'.format(g.adj))

def DFS_visita(g, u, pai, d, f, visitado):
    global tempo
    visitado[u] = True
    tempo+=1 #marca o tempo para saber em qual tempo cada vértice foi descoberto e terminado
    d[u] = tempo #registra o tempo que o vértice u foi descoberto
    for w in g.adj[u]:
        if not visitado[w]:
            pai[w] = u
            DFS_visita(g, w, pai, d, f, visitado) 
    
    tempo +=1
    f[u] = tempo #registra o tempo em que o vértice foi inteiramente examinado, ou seja, todas as adjancencias desse vértice ja foram visitadas

lista_caminho = []
def caminho(v1, v2, g): #esta função retorna o caminho de v1 até v2 no grafo g
    global lista_caminho
    for vertice in range(v1, len(g.adj)-1):
        if vertice == len(g.adj)-1:
            return lista_caminho
        else:
            for aresta in g.adj[vertice]:
                lista_caminho.append(aresta)
    for v in lista_caminho:
            print(v, end="  -> ")
        
                
            
            



#main
arestas = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (3, 7), (4, 5), (5, 6), (6, 7)]
digrafo = grafo_direcionado(7)
for e in arestas:
    digrafo.insere(e[0], e[1])

DFS(digrafo)
caminho(0, 6, digrafo)
