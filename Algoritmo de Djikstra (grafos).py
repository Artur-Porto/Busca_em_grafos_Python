# Função que detecta os vértices adjacentes de um dado vértice em G ------------
def adjacentes(v, G):
  (V, E, w) = G
  adj = []
  for aresta in E: # Conferir em todas as arestas
    (pred, suc) = aresta 
    if v == pred: # Se a aresta é tal que v é o primeiro vértice
      adj.append(suc) # Então suc é seu sucessor / adjacente
  return adj # Lista de adjacentes
# ------------------------------------------------------------------------------

# Função dedicada a retirar o vértice de menor chave de Q ----------------------
def retire_vertice_menor_chave(Q):
  menor_vertice = list(Q.keys())[0]
  menor_chave   = Q[menor_vertice]

  # Busca pela menor chave
  for vertice in Q:
    chave = Q[vertice]
    if chave < menor_chave:
      menor_chave   = chave
      menor_vertice = vertice
  
  # Retirada do vértice do dicionário
  chave_x_valor = Q.pop(menor_vertice)
  return menor_vertice
# ------------------------------------------------------------------------------

# Algoritmo de Prim para detecção de árvore geradora mínima --------------------
from math import inf

def Djikstra(G,raiz):
  (V,E,w) = G
  chave = {}
  predecessor = {}
  for v in V:
      chave[v] = inf
      predecessor[v] = ''
      
  chave[raiz] = 0
  Q = {v:chave[v] for v in V}
  while len(Q) > 0:
    v = retire_vertice_menor_chave(Q)
    print('---------',v,'-----------')
    for u in adjacentes(v, G):

      d = chave[v] + w(v,u)
      if d < chave[u]: # Relaxação
        print('Antes: w(',v,',',u,') = ',w(v,u),' e chave[',u,'] = ',chave[u])
        predecessor[u] = v
        chave[u] = d
        Q[u] = d
        print('Depois: w(',v,',',u,') = ',w(v,u),' e chave[',u,'] = ',chave[u])

  return predecessor, chave

V = ['V0', 'V1', 'V2', 'V3', 'V4']

E = [ ('V0','V0'), ('V0','V1'), ('V0','V2'),('V0','V3'),('V0','V4'),
     ('V1','V0'), ('V1','V1'), ('V1','V2'),('V1','V3'),('V1','V4'),
     ('V2','V0'), ('V2','V1'), ('V2','V2'),('V2','V3'),('V2','V4'),
     ('V3','V0'), ('V3','V1'), ('V3','V2'),('V3','V3'),('V3','V4'),
     ('V4','V0'), ('V4','V1'), ('V4','V2'),('V4','V3'),('V4','V4'),]

W = [6, 66, 89, 23, 7,  
     25, 1, 36, 37, 35,
     43, 29, 4, 13, 39,
     59, 8, 42, 73, 39,  
     94, 100, 4, 96, 10]

def w(u,v):
  return W[E.index((u,v))]

G = (V,E,w)


predecessor, chave = Djikstra(G,'V0')

print(predecessor)
print(chave)