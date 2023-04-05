import Leitor
from Vulnerabilidade import Vuln
teste = Vuln( 'bcopy', 'BufferOverflow', 'Falha em garantir que o caracter de terminação nao se encontra presente no destino. Uma solucao que melhora substancialmente o problema e utilizar o memcpy().')

print(teste.funcao)
print(teste.tipo)
print(teste.descricao)
