from typing_extensions import Self


class Funcionario :
    def __init__(self, cpf, nome, dataNascimento, salario):
        self.__cpf = cpf
        self.__nome = nome
        self.__dataNascimento = dataNascimento
        self.__salario = salario
    def getCpf(self):
        return self.__cpf
    
    def setCpf(self, cpf):
        self.__cpf = cpf
    
    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome
        
    def getDataNascimento(self):
        return self.__dataNascimento
    
    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento
        
    def getSalario(self):
        return self.__salario
    
    def setSalario(self, salario):
        self.__salario = salario

    