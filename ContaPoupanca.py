import Conta

class ContaPoupanca(Conta.ContaPoupanca):
    def __init__(self, titular, numeroConta, saldo, taxaDiaria):
        super().__init__(titular, numeroConta, saldo)
        self.__taxaDiaria = taxaDiaria

    def getTaxaDiaria(self):
        return self.__taxaDiaria
    
    def setTaxaDiaria(self, taxaDiaria):
        self.__taxaDiaria = taxaDiaria