import sys
def leArquivo():
     #Verifica se um argumento foi passado na linha de comando
    if len(sys.argv) < 2:
        print("Por favor, informe o nome do arquivo como argumento.")
        sys.exit()

    # Obtém o nome do arquivo a partir do segundo argumento
    nome_arquivo = sys.argv[1]
    lista_strings = []

    # Abre o arquivo e lê suas linhas
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            if any(string in linha for string in lista_strings):
                print("teste concluido ")
            else:
                nada = 0
      
leArquivo()
