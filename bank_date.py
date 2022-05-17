import mysql.connector
from mysql.connector import Error

titular = "gabriel"
numero = '1'
saldo = '23.50'

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


def insertTable () : #inserir na tabela
 
  dados = numero+ ',\''+titular+ '\','+saldo+ ')'
  declaracao = """INSERT INTO contacorrente (numeroConta, titular, saldo) VALUES ("""
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
  
def consult(numeroConta) : #consultar a tabela
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
      
  except Error as erro:
    print("falha ao consultar dado", format(erro))
    
  #finally:
  if(con.is_connected()) :
    cursor.close()
    con.close()

#------------------------------------------------------------------------------------


def updateTable (declaracao) : #vai atualizar a tabela
  try:
    conected()
    altera_conta = declaracao
    cursor = con.cursor()
    cursor.execute(altera_conta)
    con.commit()
    print("preco alterado com sucesso!")
    
  except Error as erro:
    print("falha ao alterar tabela", format(erro))
  
  finally:
    if(con.is_connected()) :
      cursor.close()
      con.close()
#---------------------------------------------------------------------------------------      
  
if __name__=='__main__':
  print("atualizar preco de produtos no banco de dados")
  print("entre com os dados conforme solicitado:")
  
  
  numeroConta = '1' #input("digite o numero da sua conta: ")
  consult(numeroConta)
  
  print("digite quanto quer depositar: ")
  deposito = '25.00'
  
  declaracao = """UPDATE contacorrente"""
  
  