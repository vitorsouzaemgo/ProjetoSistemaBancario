CREATE TABLE contaCorrente (
	`numeroConta` int not null,
    `titular` varchar(80),
    `saldo` real,

    primary key(numeroConta)
);

CREATE TABLE contaPoupanca (
	`numeroConta` integer not null,
    `titular` varchar(80),
    `saldo` real,
    `tavaDiaria` real,
	primary key(numeroConta)
);

CREATE TABLE `deposito` (
  `numeroDeposito` int NOT NULL,
  `numeroConta` int NOT NULL,
  `titular` varchar(80) DEFAULT NULL,
  `saldo` double DEFAULT NULL,
  `valorDeposito` double DEFAULT NULL,
  PRIMARY KEY (`numeroDeposito`)
);