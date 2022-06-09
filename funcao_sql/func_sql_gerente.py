from distutils.log import error
import bank_date as bank_date
from mysql.connector import Error


def CriaNovaConta (titular, senha, cpf, tipoConta) : #vai criar conta

  try:
    con = bank_date.conected()
    cursor = con.cursor()
     
    if tipoConta == 'contaCorrente' :
      declaracao = f'INSERT INTO `contasbancarias`.`contaCorrente` ( `titular`, `saldo`, `senha`, `cpf`) VALUES ( "{titular}", 0, "{senha}", "{cpf}");'
    elif tipoConta == 'contaPoupanca' :
      declaracao = f'INSERT INTO `contasbancarias`.`contapoupanca` ( `titular`, `saldo`, `taxaDiaria`, `senha`, `cpf`) VALUES ( "{titular}", 0, "2.5", "{senha}", "{cpf}");'
    
    cursor.execute(declaracao)
    con.commit()
    
  except Error as erro:
    print('falha ao inserir dados na tabela', format(erro))
  
  finally:
    if con.is_connected() :
      cursor.close()
      con.close()
      print("conexao ao MySql foi encerrada")

def consultaConta (numeroAgencia):
  
  try:
    con = bank_date.conected()
    cursor = con.cursor()
    declaracao = f'SELECT * FROM `contasBancarias`.`contacorrente` WHERE agencia={numeroAgencia}'
    cursor.execute(declaracao)
    linhas = cursor.fetchall()
    
    for linha in linhas:
      print(linha)
    return linhas
  except Error as erro :
    print('falha ao inserir dados da tabela', format(erro))
  
  finally:
    if con.is_connected():
      cursor.close()
      con.close()
      print('conexao ao MySql foi encerrada')
      
      
#testagem da funcao
if __name__=='__main__':
  titular = 'Odara'
  senha = '12345678'
  cpf = '87689055433'
  conta = '13'
  CriaNovaConta(titular, senha, cpf, 'contaPoupanca')
  
  #consultaConta(conta)
  
  
