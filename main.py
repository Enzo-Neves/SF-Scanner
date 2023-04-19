import sys
from Leitor import leArquivo
from Leitor import criaWordList

print('')
print('')

if len(sys.argv) < 2:
    print("Por favor, informe o nome do arquivo como argumento.")
    sys.exit()

listadevulnerabilidades = criaWordList(wordlist = sys.argv[2] )

leArquivo(arquivoAnalise = sys.argv[1], listadevulnerabilidades= listadevulnerabilidades)


