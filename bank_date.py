import mysql.connector
from mysql.connector import Error
from sqlalchemy import true




def conected() : #vai conectar o algoritmo ao banco de dados
  try:
    global con
    con = mysql.connector.connect(host='localhost', database='contasBancarias', user='root', password='12345678')
    #host: se for um banco de dados que nao e local, precisa colocar o endereco da maquina em host
    #database: nome do banco de dados
    #user: o usuario que vai acessar o banco de dados
    #password: senha do banco de dados
    
    if con.is_connected():
      print("conectado ao servidor MySQL", con.get_server_info())

  except Error as erro:
    print("falha ao inserir dados no MySQL: ", format(erro))
#--------------------------------------------------------------------------------


def insertTable (numeroConta, titular, saldo, senha, cpf) : #inserir na tabela
 
  dados = numeroConta+ ',\''+titular+ '\','+saldo+ '\','+senha+'\','+cpf+')'
  declaracao = """INSERT INTO contacorrente (numeroConta, titular, saldo, senha, cpf) VALUES ("""
  sql = declaracao + dados

  if con.is_connected(): 
    print("conectado ao servidor MySQL ", con.get_server_info())
    cursor = con.cursor()
    #objeto que permite fazer a interacao para os elementos de uma tabela retornados
    cursor.execute(sql)
    con.commit()
    print(cursor.rowcount, "registros inseridos na tabela")
      # linha = cursor.fetchone()
      #fetchone: vai buscar uma linha
      # print("conectado ao banco de dados", linha)
      

      #ele vai verificar se a conexao
     
      
    if con.is_connected() :
      cursor.close()
      con.close()
      print("conexao ao MySql foi encerrada")
#----------------------------------------------------------------------------------


def consult(numeroConta) : #consultar a tabela, vai consultar apartir do numero da conta do usuario, vai retornar o saldo do usuario
  try:
    conected()
    consulta_sql = 'SELECT * from contacorrente WHERE numeroConta = '+numeroConta
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall() #retorna as linha da tabela

    for linha in linhas:
      print("numero conta: ", linha[0])
      print("titular: ", linha[1])
      print("saldo", linha[2])
    
    return linha[2]
  except Error as erro:
    print("falha ao consultar dado", format(erro))
    
  finally:
    if(con.is_connected()) :
      cursor.close()
      con.close()
#------------------------------------------------------------------------------------


def updateTable (numeroConta, deposito, saldoAnterior, escolha) : #vai atualizar a tabela, no caso ele vai atualizar o saldo do cliente
  
  if escolha : #se for depositar ele vai somar o valor do deposito com o que ja tem na conta
    deposito=float(deposito) + float(saldoAnterior)
    deposito = str(deposito)
    print(deposito)
  else : #se for retirar dinheiro ele vai retirar o valor que ja ta na conta
    deposito=float(saldoAnterior)-float(deposito) 
    deposito = str(deposito)
    print(deposito)
    
    
    
  declaracao = """UPDATE contacorrente SET saldo ="""+deposito+ """ WHERE numeroConta = """+numeroConta
  
  try:
    conected()
    
    cursor = con.cursor()
    cursor.execute(declaracao)
    con.commit()
    print("deposito alterado com sucesso!")
    
  except Error as erro:
    print("falha ao alterar tabela", format(erro))
  
  finally:
    if(con.is_connected()) :
      cursor.close()
      con.close()
#---------------------------------------------------------------------------------------      
  
if __name__=='__main__':
  print("entre com os dados conforme solicitado: ")
  
  #valores iniciais para teste
  titular = 'gabriel'
  deposito = '55.00'
  numeroConta = '1'
  saldo='0'
  senha='12345678'
  cpf='11111111111'
  
  insertTable (numeroConta, titular, saldo, senha, cpf)
  escolha = true
  
  saldoAnterior = consult(numeroConta)
  
  print("digite quanto quer depositar: ")
  print("saldo da conta: ", saldoAnterior)
  
  
  updateTable(numeroConta, deposito, consult(numeroConta), escolha)
  