import bank_date as bank_date
from mysql.connector import Error
import PySimpleGUI as sg

def deposito (cpf, valor, tipoConta) : #vai atualizar a tabela, no caso ele vai atualizar o saldo do cliente
    
  contaLinha=bank_date.consult(cpf, tipoConta) #vai pegar o cadastro e retornar a linha
  conta = f'UPDATE `contasbancarias`.`{tipoConta}` SET saldo = saldo + {valor} WHERE cpf = "{cpf}"'#vai atualizar o saldo na conta
  valor = f'VALUE ("{contaLinha[0]}", "{contaLinha[1]}", "{contaLinha[2]}", "{valor}", "1")'#vai pegar os dados do cadastro para ser inserido na tabela de extrato
  extrato = 'INSERT INTO `contasbancarias`.`extrato` (`numeroConta`, `titular`, `saldo`, `valorDeposito`, `tipoOperacao`) '+valor
   
  try:
    con = bank_date.conected()
    
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
      
      
      
def saque (cpf, valor) : #vai atualizar a tabela após fazer o saque
  
  con = bank_date.conected()
  saldo1 = bank_date.consult(cpf)[2]
  cheque = bank_date.consult(cpf)[5]
  if(valor > (saldo1 + cheque)):
    sg.popup('Valor de saque indisponível', title='Falha no Saque', font='Verdana')
  elif(valor > saldo1 and valor <= (saldo1+cheque)):
    cursor = con.cursor()
    if(con.is_connected()) :
      cheque1 = (cheque - (valor - saldo1))
      declaracao1 = f'UPDATE contaCorrente SET saldo = 0 WHERE cpf = '+cpf
      declaracao2 = f'UPDATE contaCorrente SET chequeEspecial = {cheque1} WHERE cpf = '+cpf
      cursor.execute(declaracao1)
      cursor.execute(declaracao2)
      con.commit()
      
  elif(valor > 0 and valor <= saldo1):
    
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

    
def extrato (numeroConta) :
    sql = f'Select * from contasbancarias.extrato WHERE numeroConta={numeroConta}'
    try:
        con = bank_date.conected()
        cursor = con.cursor()
        cursor.execute(sql)
        linhas = cursor.fetchall()
        
        for linha in linhas:
          print('numero da operacao: ', linha[0])
          print('saldo: ', linha[3])
          
          if linha[5] == 1:
            print('valor do deposito', linha[4])
            resultado = int(linha[3]) + int(linha[4])
          elif linha[5] == 2:
            print('valor do saque', linha[4])
            resultado = int(linha[3]) - int(linha[4])
          
          print('saldo atual: ', resultado)
          print('---------------------------------')
        return linhas
        
    except Error as erro:
        print("falha ao alterar tabela", format(erro))
  
    finally:
        if(con.is_connected()) :
            cursor.close()
            con.close()
      
        
#testagem da funcao       
if __name__=='__main__':
    #linhas = extrato('1')
    cpf='08016650350'
    valor='200'
    tipoConta='contacorrente'
    deposito(cpf, valor, tipoConta)
    
    
    
        