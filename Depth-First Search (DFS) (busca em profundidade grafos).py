
# Função que detecta os vértices adjacentes de um dado vértice em G ------------
def adjacentes(v, G):
  (V, E, w) = G
  adj = []
  for aresta in E: # Conferir em todas as arestas
    (pred, suc) = aresta 
    if v == pred: # Se a aresta é tal que v é o primeiro vértice
      adj.append(suc) # Então suc é seu sucessor / adjacente
  return adj # Lista de adjacentes

def push_pilha(Q, elemento):
  Q.insert(0,elemento)

def pop_pilha(Q):
  return Q.pop(0)

from math import inf
def DFS(G,raiz, valor_procurado):
  (V,E,w) = G
  existe = False
  distancia = {}
  predecessor = {}
  cores = {}
  for v in V:
      distancia[v] = inf
      predecessor[v] = ''
      cores[v] = 'BRANCO'
      
  distancia[raiz] = 0
  cores[raiz] ='CINZA'
  Q = [] # Fila Vazia
  lista_de_visitacao = []
  push_pilha(Q,raiz) # Insere a raiz na pilha
  while len(Q) > 0:

    v = pop_pilha(Q) # Remove o elemento mais recente da estrutura

    if v == valor_procurado: # Verifica a existência
      existe = True

    cores[v] = 'PRETO' # Vértice já visitado
    lista_de_visitacao.append(v)


    print('---------',v,'-----------')
    for u in adjacentes(v, G):

      if cores[u] == 'BRANCO': # Vértice ainda não visitado
        distancia[u] = distancia[v] + 1 # Acumula a distância
        predecessor[u] = v # Atualiza o predecessor

        cores[u] = 'CINZA' # Vértice já considerado
        push_pilha(Q,u)     # Empilha



  return distancia, predecessor, existe, lista_de_visitacao



V = ['A','B','C','D','E','F','G','H','I','J']
E = [('A','B'), ('B','A'), ('A','C'), ('C','A'), ('A','D'),('D','A'),
     ('B','E'), ('E','B'), ('C','F'), ('F','C'), ('D','G'), ('G','D'),
     ('E','H'), ('H','E'),('E','I'),('I','E'),('F','J'),('J','F'),('G','J'),('J','G')]
W = [1,1,1,1,1,1,
     1,1,1,1,1,1,
     1,1,1,1,1,1,1,1]
     
def w(u,v):
  return W[E.index((u,v))]
  
G = (V,E,w)

distancia, predecessor, existe, lista_de_visitacao = DFS(G, 'A', 'J')
print()
print(lista_de_visitacao)