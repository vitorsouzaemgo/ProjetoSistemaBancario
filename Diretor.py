import Funcionario

class Diretor(Funcionario.Diretor) :
    def __init__(self, cpf, nome, dataNascimento, salario):
        super().__init__(cpf, nome, dataNascimento, salario)

    def getSalario(self):
        return self.__salario
    
    def setSalario(self, salario):
        self.__salario = salario * 1.4