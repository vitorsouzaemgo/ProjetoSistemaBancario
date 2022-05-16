import Conta

class ContaCorrente(Conta.ContaCorrente):
    def __init__(self, titular, numeroConta, saldo, chequeEspecial):
        super().__init__(titular, numeroConta, saldo)
        self.__chequeEspecial = chequeEspecial
    
    def getChequeEspecial(self):
        return self.__chequeEspecial
    
    def setChequeEspecial(self, chequeEspecial):
        self.__chequeEspecial = chequeEspecial
    
