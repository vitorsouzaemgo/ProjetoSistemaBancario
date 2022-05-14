class Conta:
    def __init__(self, titular, numeroConta, saldo):
        self.__titular = titular
        self.__numeroConta = numeroConta
        self.__saldo = saldo

    def getTitular(self):
        return self.__titular
    
    def getTitular(self, titular):
        self.__titular = titular

    def getNumeroConta(self):
        return self.__numeroConta
    
    def getTitular(self, numeroConta):
        self.__numeroConta = numeroConta

    def getTitular(self):
        return self.__saldo
    
    def getTitular(self, saldo):
        self.__saldo = saldo