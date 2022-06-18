import PySimpleGUI as sg
import random

from sqlalchemy import null
import funcao_sql.bank_date as bank_date

def validadeCPF(cpf):
    if len(cpf) != 11:
        sg.popup('Tamanho de CPF inválido', title='Falha no Cadastro', font='Verdana')
        print(len(cpf))
    elif len(cpf)==11:
        temp = [ord(cpf[0]), ord(cpf[1]), ord(cpf[2]), ord(cpf[3]), ord(cpf[4]), ord(cpf[5]), ord(cpf[6]), ord(cpf[7]), ord(cpf[8])]
        soma1 = ((temp[0]-48)*10) + ((temp[1]-48)*9) + ((temp[2]-48)*8) + ((temp[3]-48)*7) + ((temp[4]-48)*6) + ((temp[5]-48)*5) + ((temp[6]-48)*4) + ((temp[7]-48)*3) + ((temp[8]-48)*2)
        if (11-(soma1%11)) >= 10: 
            resultado1 = 0
        else:
            resultado1 = (11-(soma1%11))

        if resultado1 != ord(cpf[9])-48:
            sg.popup('Número de CPF inválido', title='Falha no Cadastro', font='Verdana')
        else:
            soma2 = ((ord(cpf[0])-48)*11) + ((ord(cpf[1])-48)*10) + ((ord(cpf[2])-48)*9) + ((ord(cpf[3])-48)*8) + ((ord(cpf[4])-48)*7) + ((ord(cpf[5])-48)*6) + ((ord(cpf[6])-48)*5) + ((ord(cpf[7])-48)*4) + ((ord(cpf[8])-48)*3) + ((ord(cpf[9])-48)*2)
            if (11-(soma2%11)) >= 10:
                resultado2 = 0
            else:
                resultado2 = (11-(soma2%11))

            if resultado2 != ord(cpf[10])-48:
                sg.popup('Número de CPF inválido', title='Falha no Cadastro', font='Verdana')
            else:
                return True
