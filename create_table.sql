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
