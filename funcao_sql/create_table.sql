/*criacao da tabela*/
CREATE TABLE `contacorrente` (
  `numeroConta` int NOT NULL AUTO_INCREMENT,
  `titular` varchar(80) NOT NULL,
  `saldo` double DEFAULT '0',
  `senha` varchar(45) NOT NULL,
  `cpf` varchar(45) NOT NULL,
  `agencia` int NOT NULL, 
  PRIMARY KEY (`numeroConta`, `cpf`)
);
/*valores para testar nas funções*/
INSERT INTO `contabancarias`.`contacorrente` (`numeroConta`,`titular`,`saldo`,`senha`,`cpf`,`agencia`) VALUES (1,'gabriel',110,'12345678','08016650350',13);
INSERT INTO `contabancarias`.`contacorrente` (`numeroConta`,`titular`,`saldo`,`senha`,`cpf`,`agencia`) VALUES (2,'vitor',50,'12345678','75643509644',13);
INSERT INTO `contabancarias`.`contacorrente` (`numeroConta`,`titular`,`saldo`,`senha`,`cpf`,`agencia`) VALUES (3,'luan',200,'12345678','35689046790',13);
INSERT INTO `contabancarias`.`contacorrente` (`numeroConta`,`titular`,`saldo`,`senha`,`cpf`,`agencia`) VALUES (4,'natan',500,'12345678','10293847562',12);
INSERT INTO `contabancarias`.`contacorrente` (`numeroConta`,`titular`,`saldo`,`senha`,`cpf`,`agencia`) VALUES (5,'melissa',200,'12345678','10293847561',12);
INSERT INTO `contabancarias`.`contacorrente` (`numeroConta`,`titular`,`saldo`,`senha`,`cpf`,`agencia`) VALUES (6,'joao manoel',400,'12345678','43560030501',12);
INSERT INTO `contabancarias`.`contacorrente` (`numeroConta`,`titular`,`saldo`,`senha`,`cpf`,`agencia`) VALUES (7,'Odara',0,'12345678','87689055433',14);
INSERT INTO `contabancarias`.`contacorrente` (`numeroConta`,`titular`,`saldo`,`senha`,`cpf`,`agencia`) VALUES (8,'Odara',0,'12345678','87689055433',14);

CREATE TABLE `contapoupanca` (
  `numeroConta` int NOT NULL,
  `titular` varchar(80) DEFAULT NULL,
  `saldo` double DEFAULT NULL,
  `taxaDiaria` double DEFAULT NULL,
  `senha` varchar(45) DEFAULT NULL,
  `cpf` varchar(45) DEFAULT NULL,
  `agencia` int NOT NULL,
  PRIMARY KEY (`numeroConta`)
) ;

/*criacao da tabela*/
CREATE TABLE extrato (
  `numeroOperacao` int NOT NULL,
  `numeroConta` int NOT NULL,
  `titular` varchar(80) DEFAULT NULL,
  `saldo` double DEFAULT NULL,
  `valorDeposito` double DEFAULT NULL,
  `tipoOperacao` int NOT NULL 
  PRIMARY KEY (`numeroOperacao`)
);

/*valores para testar a funcao*/
INSERT INTO `contabancarias`.`extrato` (`numeroOperacao`,`numeroConta`,`titular`,`saldo`,`valorDeposito`,`tipoOperacao`) VALUES (1,1,'gabriel',200,400,1);
INSERT INTO `contabancarias`.`extrato` (`numeroOperacao`,`numeroConta`,`titular`,`saldo`,`valorDeposito`,`tipoOperacao`) VALUES (2,1,'gabriel',600,400,1);
INSERT INTO `contabancarias`.`extrato` (`numeroOperacao`,`numeroConta`,`titular`,`saldo`,`valorDeposito`,`tipoOperacao`) VALUES (3,1,'gabriel',1000,400,1);
INSERT INTO `contabancarias`.`extrato` (`numeroOperacao`,`numeroConta`,`titular`,`saldo`,`valorDeposito`,`tipoOperacao`) VALUES (4,1,'gabriel',1400,200,2);
INSERT INTO `contabancarias`.`extrato` (`numeroOperacao`,`numeroConta`,`titular`,`saldo`,`valorDeposito`,`tipoOperacao`) VALUES (5,1,'gabriel',1200,800,1);
INSERT INTO `contabancarias`.`extrato` (`numeroOperacao`,`numeroConta`,`titular`,`saldo`,`valorDeposito`,`tipoOperacao`) VALUES (6,2,'vitor',800,200,1);
INSERT INTO `contabancarias`.`extrato` (`numeroOperacao`,`numeroConta`,`titular`,`saldo`,`valorDeposito`,`tipoOperacao`) VALUES (7,2,'vitor',1000,200,1);


CREATE TABLE gerente (
  `numeroCPF` int NOT NULL,
  `senha` varchar(80) NOT NULL,
  `agencia` int NOT NULL,
  PRIMARY KEY (`numeroCPF`)
);

CREATE TABLE diretor (
  `numeroCPF` int NOT NULL,
  `senha` varchar(80) NOT NULL,
  primary key(`numeroCPF`)
);
