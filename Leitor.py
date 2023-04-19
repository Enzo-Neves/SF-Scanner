import sys
from Vulnerabilidade import Vuln
from Vulnerabilidade import Vuln
def leArquivo(arquivoAnalise, listadevulnerabilidades):
    # Abre o arquivo e lê suas linhas

    qtdFuncoes= len(listadevulnerabilidades)
    descobertas = 0
    with open(arquivoAnalise, 'r') as arquivo:
        for elemento in listadevulnerabilidades:
            for linha in arquivo:
    
                if elemento.funcao in linha:
                    print('Foi encontrada a seguinte função vulneravel: ' +elemento.funcao + '\n Tipo:' + elemento.tipo + '\n Descrição' + elemento.descricao)
                
                    descobertas += 1
        if descobertas == 0: 
            print('Nao foi encontrada nenhuma vulnerabilidade')

def criaWordList(wordlist):
    listadevulnerabilidades = []
    with open (wordlist , 'r') as arquivo:
        for linha in arquivo:
            split = linha.split(";")
            vuln = Vuln(split[0], split[1] , split [2])
            listadevulnerabilidades.append(vuln)
            
    return listadevulnerabilidades

            
