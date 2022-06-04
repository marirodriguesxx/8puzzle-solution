from Posicao import Posicao
from AEstrela import AEstrela
from QuebraCabeca import QuebraCabeca
from QuebraCabecaImp import QuebraCabecaImp
import math
import queue
import heapq
from random import gammavariate, shuffle



class AEstrelaImp(AEstrela):
    def getHeuristica(node):
        tableGab = node.tabGabarito
        currentTable = node.getTab()
        heuristica = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if tableGab[i][j] != currentTable[i][j]:
                    heuristica += node.getValor()                  
        return heuristica

    def getSolucao(self, qc):

        codUnique = set()
        codUnique.add(qc.hashCode())
        
        tableGab = qc.tabGabarito 
        tableRoot = qc.getTab() 
        
        goal = 1 
        emptyPosition = []

        
        if(tableRoot == tableGab):
            return emptyPosition
        else:
            F = getHeuristica(qc) + goal 
            gameInfo = [[ F, goal, tableRoot ]] 

        while(gameInfo):

            if(qc.getTab() == tableGab):
                break 

            lista_movimentos = qc.getMovePossiveis()
            pos_vazio = qc.getPosVazio()           
            
            for movimento in lista_movimentos:
                qc.move(pos_vazio.getLinha(), pos_vazio.getColuna(), movimento.getLinha(), movimento.getColuna())
                tableAux = qc.getTab()
                
                if qc.hashCode() not in codUnique: 
                    codUnique.add(qc.hashCode()) 
                    function_H = getHeuristica(qc)
                    gameInfo.append([(function_H + goal + 1), goal + 1, tableAux])
               
                qc.move(movimento.getLinha(), movimento.getColuna(), pos_vazio.getLinha(), pos_vazio.getColuna())

            gameInfo.pop(0)
            gameInfo.sort()
            qc.setTab(gameInfo[0][2])
            emptyPosition.append(qc.getPosVazio())

        return emptyPosition   