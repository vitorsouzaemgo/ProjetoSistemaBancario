import Funcionario

class Gerente(Funcionario.Gerente) :
    def __init__(self, cpf, nome, dataNascimento, salario, agencia):
        super().__init__(cpf, nome, dataNascimento, salario, agencia)
        self.__agencia = agencia
    
    def getAgencia(self):
        return self.__agencia
    
    def setAgencia(self, agencia):
        self.__agencia = agencia
    
    def getSalario(self):
        return self.__salario
    
    def setSalario(self, salario):
        self.__salario = salario * 1.2
