import mysql.connector
from mysql.connector import Error


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

def consultTable(numero) : #consultar a tabela, vai consultar apartir do numero da conta do usuario, vai retornar o saldo do usuario
    
  conected()
  consulta_sql = f'SELECT * from contaCorrente WHERE numeroConta = {numero}'
  cursor = con.cursor()
  cursor.execute(consulta_sql)
  numero = cursor.fetchone() #retorna as linha da tabela  

  if(con.is_connected()):
    cursor.close()
    con.close() 

  return numero
  