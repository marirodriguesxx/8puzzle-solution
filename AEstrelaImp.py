from Posicao import Posicao
from AEstrela import AEstrela
from QuebraCabeca import QuebraCabeca
from QuebraCabecaImp import QuebraCabecaImp

def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def isSolvable(puzzle) :
 
    # Count inversions in given 8 puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub])
 
    # return true if inversion count is even.
    return (inv_count % 2 == 0)


class AEstrelaImp(AEstrela):
    def getSolucao(self, qc):

        if (not isSolvable(qc.getTab())):
            print("Sem solução")
            return 

        configsVisitadas = []
        posVazia = []
        configsVisitadas.append(qc.hashCode())
        g = 1 
        f = qc.getValor() + g 
        gameInfo = [[ f, g, qc.getTab() ]] 

        while(qc.getTab() != qc.tabGabarito):
            movimentos = qc.getMovePossiveis() #uma lista de posições de movimentos possiveis
            vazio = qc.getPosVazio()         #coordenadas da posicao vazia
            
            for destino in movimentos:
                qc.move(vazio.getLinha(), vazio.getColuna(), destino.getLinha(), destino.getColuna()) #move o vazio
                tableAux = qc.getTab()
                #calcula o caminho
                if qc.hashCode() not in configsVisitadas: #se ainda nao verificamos essa config de tabuleiro
                    configsVisitadas.append(qc.hashCode()) #marcamos como verificada, adicionando ao vetor de visitados
                    f = qc.getValor() + (g +1) #mais um nivel na arvore 
                    gameInfo.append([f, g , tableAux])
                #retorna pra posicao
                qc.move(destino.getLinha(), destino.getColuna(), vazio.getLinha(), vazio.getColuna())

            gameInfo.pop(0)
            gameInfo.sort() # ordena de acordo com o valor do custo total do caminho
            qc.setTab(gameInfo[0][2])
            posVazia.append(qc.getPosVazio())

        return posVazia   