import Funcionario

class CaixaDeBanco(Funcionario.CaixaDeBanco) :
    def __init__(self, cpf, nome, dataNascimento, agencia):
        super().__init__(cpf, nome, dataNascimento, agencia)
        self.__agencia = agencia
    
    def getAgencia(self):
        return self.__agencia
    
    def setAgencia(self, agencia):
        self.__agencia = agencia


        