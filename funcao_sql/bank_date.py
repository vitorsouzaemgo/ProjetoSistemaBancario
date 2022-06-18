import mysql.connector
from mysql.connector import Error
import PySimpleGUI as sg
import random


def conected() : #vai conectar o algoritmo ao banco de dados
  try: 
    global con
    con = mysql.connector.connect(host='localhost', database='contasbancarias', user='root', password='12345678')
    #host: se for um banco de dados que nao e local, precisa colocar o endereco da maquina em host
    #database: nome do banco de dados
    #user: o usuario que vai acessar o banco de dados
    #password: senha do banco de dados

  except Error as erro:
    print("falha ao inserir dados no MySQL: ", format(erro))
  
  return con

def consult(cpf, tipoConta) : #consultar a tabela, vai consultar apartir do numero da conta do usuario, vai retornar o saldo do usuario
  try:
    conected()
    consulta_sql = f'SELECT * from contasbancarias.{tipoConta} WHERE cpf = {cpf}'
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linha = cursor.fetchone() #retorna as linha da tabela
    
    return linha
  except Error as erro:
    print("falha ao consultar dado", format(erro))
    
  finally:
    if(con.is_connected()):
      cursor.close()
      con.close()
#------------------------------------------------------------------------------------

# def consultTable(numero) : #consultar a tabela, vai consultar apartir do numero da conta do usuario, vai retornar o saldo do usuario
    
#   conected()
#   consulta_sql = f'SELECT * from contacorrente WHERE numeroConta = {numero}'
#   cursor = con.cursor()
#   cursor.execute(consulta_sql)
#   numero = cursor.fetchone() #retorna as linha da tabela  

#   if(con.is_connected()):
#     cursor.close()
#     con.close() 

#   return numero

#------------------------------------------------------------------------------------

def CriaNovaConta (titular, senha, cpf, tipoConta) : #vai criar conta

  x = random.randint(10000000,99999999)

  try:
    conected()
    cursor = con.cursor()
     
    if tipoConta == 'contacorrente' :
      declaracao = f'INSERT INTO `contasbancarias`.`contacorrente` ( `numeroConta`,`titular`, `saldo`, `senha`, `cpf`) VALUES ( {x}, "{titular}", 0, "{senha}", "{cpf}");'
    elif tipoConta == 'contapoupanca' :
      declaracao = f'INSERT INTO `contasbancarias`.`contapoupanca` ( `numeroConta`,`titular`, `saldo`, `taxaDiaria`, `senha`, `cpf`) VALUES ( {x}, "{titular}", 0, "0.01", "{senha}", "{cpf}");'
    
    print('Conta criada com sucesso!')
    cursor.execute(declaracao)
    con.commit()
    
  except Error as erro:
    print('falha ao inserir dados na tabela', format(erro))
  
  finally:
    if con.is_connected() :
      cursor.close()
      con.close()
      print("conexao ao MySql foi encerrada")

#------------------------------------------------------------------------------------

def deposito (cpf, valor, tipoConta) : #vai atualizar a tabela, no caso ele vai atualizar o saldo do cliente
    
  contaLinha=consult(cpf, tipoConta) #vai pegar o cadastro e retornar a linha
  conta = f'UPDATE `contasbancarias`.`{tipoConta}` SET saldo = saldo + {valor} WHERE cpf = "{cpf}"'#vai atualizar o saldo na conta
  valores = f'VALUES ("{contaLinha[0]}", "{contaLinha[1]}", "{contaLinha[2]}", "{valor}", "1", {cpf})'#vai pegar os dados do cadastro para ser inserido na tabela de extrato
  extrato = 'INSERT INTO `contasbancarias`.`extrato` (`numeroConta`, `titular`, `saldo`, `valorOperacao`, `tipoOperacao`, `cpf`) '+valores
   
  try:
    conected()
    
    cursor = con.cursor()
    cursor.execute(conta) #vai alterar o valor de saldo na tabela conta
    cursor.execute(extrato) #vai cadastrar na tabela extrato a transação
    con.commit()
    
    
    print("Saldo alterado com sucesso!")
    
    
  except Error as erro:
    print("falha ao alterar tabela", format(erro))
  
  finally:
    if(con.is_connected()) :
      cursor.close()
      con.close()

#------------------------------------------------------------------------------------

def saque (cpf, valor, tipoConta) : #vai atualizar a tabela após fazer o saque
  
  conected()
  saldo1 = consult(cpf, tipoConta)[2]
  cheque = consult(cpf, 'contacorrente')[5]
  valor1 = float(valor)
  contaLinha=consult(cpf, tipoConta) #vai pegar o cadastro e retornar a linha
  valores = f'VALUES ("{contaLinha[0]}", "{contaLinha[1]}", "{contaLinha[2]}", "{valor}", "2", {cpf})'#vai pegar os dados do cadastro para ser inserido na tabela de extrato
  extrato = 'INSERT INTO `contasbancarias`.`extrato` (`numeroConta`, `titular`, `saldo`, `valorOperacao`, `tipoOperacao`, `cpf`) '+valores
  
  if tipoConta == 'contapoupanca' and valor1 > saldo1:
    sg.popup('Valor de saque indisponível', title='Falha no Saque', font='Verdana')
  if(valor1 > float((saldo1 + cheque))):
    sg.popup('Valor de saque indisponível', title='Falha no Saque', font='Verdana')
  elif(valor1 > saldo1 and valor1 <= (saldo1+cheque)):
    conected()

    cursor = con.cursor()
    if(con.is_connected()) :
      cheque1 = (cheque - (valor1 - saldo1))
      declaracao1 = f'UPDATE contacorrente SET saldo = 0 WHERE cpf = '+cpf
      declaracao2 = f'UPDATE contacorrente SET chequeEspecial = {cheque1} WHERE cpf = '+cpf
      cursor.execute(declaracao1)
      cursor.execute(declaracao2)
      cursor.execute(extrato) #vai cadastrar na tabela extrato a transação
      con.commit()
      
  elif(valor1 > 0 and valor1 <= saldo1):
    conected()
    cursor = con.cursor()
    if(con.is_connected()) :
      valor1 = saldo1 - valor1
      declaracao3 = f'UPDATE {tipoConta} SET saldo = {valor1} WHERE cpf = '+cpf
      cursor.execute(declaracao3)
      cursor.execute(extrato) #vai cadastrar na tabela extrato a transação
      con.commit()
  
  print("Saque realizado com sucesso!")

  if(con.is_connected()) :
    cursor.close()
    con.close()
#------------------------------------------------------------------------------------

def extrato (cpf) :
  sql = f'Select * from contasbancarias.extrato WHERE cpf={cpf}'
  try:
    conected()
    cursor = con.cursor()
    cursor.execute(sql)
    linhas = cursor.fetchall()
        
    for linha in linhas:
          
      if linha[5] == 1:
        print('Tipo de Operação: Depósito')
        print('Valor do Depósito', linha[4])
        print('Saldo Anterior: ', linha[3])
        resultado = int(linha[3]) + int(linha[4])
      elif linha[5] == 2:
        print('Tipo de Operação: Saque')
        print('Valor do Saque', linha[4])
        print('Saldo Anterior: ', linha[3])
        resultado = int(linha[3]) - int(linha[4])
          
      print('Saldo Atual: ', resultado)
      print('---------------------------------')
    return linhas
        
  except Error as erro:
    print("falha ao alterar tabela", format(erro))
  
  finally:
    if(con.is_connected()) :
      cursor.close()
      con.close()
  
if __name__=='__main__':
  # extrato('1')
  # deposito('1', 500, 'contacorrente')
  saque('1', 100, 'contapoupanca')
  # CriaNovaConta('Teste1', 'senha1', 'cpf1', 'contapoupanca')