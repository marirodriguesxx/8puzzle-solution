from Posicao import Posicao
from AEstrela import AEstrela
from QuebraCabeca import QuebraCabeca
from QuebraCabecaImp import QuebraCabecaImp

def solucionavel(puzzle):

    puzzleList = [] # matriz do tabuleiro no formato de lista, para verificar todas as combinacoes
    for l in puzzle:
        puzzleList += l

    cont = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if puzzleList[j] != QuebraCabecaImp.VAZIO and puzzleList[i] != QuebraCabecaImp.VAZIO and puzzleList[i] > puzzleList[j]:
                cont += 1
    return (cont % 2 == 0) #se o numero de inversoes for par, tem solucao

class AEstrelaImp(AEstrela):
    def getSolucao(self, qc):

        if (not solucionavel(qc.getTab())):
            print("Sem solução")
            return 

        configsVisitadas = []
        posVazia = []
        configsVisitadas.append(qc.hashCode())
        g = 1 # custo da distancia entre os nós - inicialmente 1 até o próximo nó (altura da árvore)
        f = qc.getValor() + g # custo total de um nó até ao outro
        configs = [[ f, g, qc.getTab() ]] #cada configuração de tabuleiro tera essas informacoes associadas

        while(qc.getTab() != qc.tabGabarito): #enquanto nao chegarmos ao resultado
            movimentos = qc.getMovePossiveis() #uma lista de posições de movimentos possiveis
            vazio = qc.getPosVazio()         #coordenadas da posicao vazia
            
            for destino in movimentos:
                qc.move(vazio.getLinha(), vazio.getColuna(), destino.getLinha(), destino.getColuna()) #move o vazio
                tableAux = qc.getTab()
                #calcula o caminho
                if qc.hashCode() not in configsVisitadas: #se ainda nao verificamos essa config de tabuleiro
                    configsVisitadas.append(qc.hashCode()) #marcamos como verificada, adicionando ao vetor de visitados
                    f = qc.getValor() + (g +1) #mais um nivel na arvore de solucoes
                    configs.append([f, g , tableAux])
                #retorna pra posicao
                qc.move(destino.getLinha(), destino.getColuna(), vazio.getLinha(), vazio.getColuna())

            configs.pop(0)
            configs.sort() # ordena crescentemente de acordo com o valor do custo total do caminho
            qc.setTab(configs[0][2]) # escolhemos sempre o no com menor custo e exploramos ele
            posVazia.append(qc.getPosVazio())

        return posVazia   