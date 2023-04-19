
class Vuln():
    def __init__(self ,funcao, tipo, descricao):
        self.funcao = funcao
        self.tipo = tipo
        self.descricao = descricao
    
 
    def __str__(self):
        return f"=====\nFunção: {self.funcao}\nTipo: {self.tipo}\nDescrição: {self.descricao}\n=====\n"