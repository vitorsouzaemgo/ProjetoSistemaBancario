import mysql.connector
from mysql.connector import Error
import PySimpleGUI as sg

def conected() : #vai conectar o algoritmo ao banco de dados
  try:
    global con
    con = mysql.connector.connect(host='localhost', database='contasBancarias', user='root', password='12345678')
    #host: se for um banco de dados que nao e local, precisa colocar o endereco da maquina em host
    #database: nome do banco de dados
    #user: o usuario que vai acessar o banco de dados
    #password: senha do banco de dados

  except Error as erro:
    print("falha ao inserir dados no MySQL: ", format(erro))
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------


def insertTable (numeroConta, titular, senha, cpf) : #inserir na tabela

  conected()
  cursor = con.cursor()

  if con.is_connected(): 
    declaracao = f'INSERT INTO contaCorrente (numeroConta, titular, saldo, senha, cpf) VALUES ("{numeroConta}", "{titular}", 0, "{senha}", "{cpf}")'
    cursor.execute(declaracao)
    con.commit()
      
  if con.is_connected() :
    cursor.close()
    con.close()
    print("conexao ao MySql foi encerrada")
#----------------------------------------------------------------------------------


def consult(cpf) : #consultar a tabela, vai consultar apartir do numero da conta do usuario, vai retornar o saldo do usuario
  try:
    conected()
    consulta_sql = 'SELECT * from contaCorrente WHERE cpf = '+cpf
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

def consultTable(numero) : #consultar a tabela, vai consultar apartir do numero da conta do usuario, vai retornar o saldo do usuario
    
  conected()
  consulta_sql = f'SELECT * from contaCorrente WHERE numeroConta = {numero}'
  cursor = con.cursor()
  cursor.execute(consulta_sql)
  numero = cursor.fetchone() #retorna as linha da tabela  

  if(con.is_connected()):
    cursor.close()
    con.close() 

  return numero[1]
#------------------------------------------------------------------------------------


def deposito (cpf, valor) : #vai atualizar a tabela, no caso ele vai atualizar o saldo do cliente
    
  declaracao = f'UPDATE contaCorrente SET saldo = saldo + {valor} WHERE cpf = '+cpf
  
  try:
    conected()
    
    cursor = con.cursor()
    cursor.execute(declaracao)
    con.commit()
    print("Saldo alterado com sucesso!")
    
  except Error as erro:
    print("falha ao alterar tabela", format(erro))
  
  finally:
    if(con.is_connected()) :
      cursor.close()
      con.close()
#---------------------------------------------------------------------------------------      

def saque (cpf, valor) : #vai atualizar a tabela após fazer o saque
  
  saldo1 = consult(cpf)[2]
  cheque = consult(cpf)[5]
  if(valor > (saldo1 + cheque)):
    sg.popup('Valor de saque indisponível', title='Falha no Saque', font='Verdana')
  elif(valor > saldo1 and valor <= (saldo1+cheque)):
    conected()
    cursor = con.cursor()
    if(con.is_connected()) :
      cheque1 = (cheque - (valor - saldo1))
      declaracao1 = f'UPDATE contaCorrente SET saldo = 0 WHERE cpf = '+cpf
      declaracao2 = f'UPDATE contaCorrente SET chequeEspecial = {cheque1} WHERE cpf = '+cpf
      cursor.execute(declaracao1)
      cursor.execute(declaracao2)
      con.commit()
      
  elif(valor > 0 and valor <= saldo1):
    conected()
    cursor = con.cursor()
    if(con.is_connected()) :
      valor1 = saldo1 - valor
      declaracao3 = f'UPDATE contaCorrente SET saldo = {valor1} WHERE cpf = '+cpf
      cursor.execute(declaracao3)
      con.commit()
  
  print("Saque realizado com sucesso!")

  if(con.is_connected()) :
    cursor.close()
    con.close()
#---------------------------------------------------------------------------------------      
  
# if __name__=='__main__':

  # saque('0213', 1100)
  # insertTable('João', '1234', '3022')
  # print(consult('1212'))

  # print("entre com os dados conforme solicitado: ")
  
  # #valores iniciais para teste
  # # titular = 'gabriel'
  # # deposito = '55.00'
  # # numeroConta = '1'
  # # saldo='0'
  # # senha='12345678'
  # # cpf='11111111111'

  # numeroConta = 10
  # titular = 'Vitor'
  # saldo = 150.2
  # senha = 'senha123'
  # cpf = '11111111111'
  
  # insertTable (numeroConta, titular, saldo, senha, cpf)
  # # escolha = true
  
  # # saldoAnterior = consult(numeroConta)
  
  # # print("digite quanto quer depositar: ")
  # # print("saldo da conta: ", saldoAnterior)
  
  
  # # updateTable(numeroConta, deposito, consult(numeroConta), escolha)
  