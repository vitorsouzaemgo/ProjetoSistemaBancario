CREATE TABLE `contasBancarias`.`contaCorrente` (
	  `cpf` varchar(11),
    `numeroConta` varchar(10) not null,
    `titular` varchar(80),
    `saldo` real,
    `senha` varchar(20),
    `chequeEspecial` real
    `agencia` varchar(10)
    `nomeGerente` varchar(80)

    primary key(cpf)
);

CREATE TABLE `contasBancarias`.`contaPoupanca` (
    `cpf` varchar(11),
    `numeroConta` varchar(10) not null,
    `titular` varchar(80),
    `saldo` real,
    `senha` varchar(20),
    `taxaDiaria` real
    `agencia` varchar(10)
    `nomeGerente` varchar(80)
	primary key(cpf)
);

CREATE TABLE `contasBancarias`.`extrato` (
  `numeroConta` int NOT NULL,
  `operacao` varchar(20) NOT NULL,
  `titular` varchar(80) DEFAULT NULL,
  `valorOperacao` double DEFAULT NULL,
  PRIMARY KEY (`numeroConta`)
);