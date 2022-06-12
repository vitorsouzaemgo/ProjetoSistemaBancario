import PySimpleGUI as sg
from numpy import insert
import Funcoes
from funcao_sql.bank_date import *

# Layout

global cpf1
global radioLogin
global radioCadastro

def janela_inicial():
    sg.theme('Reddit')
    layout = [
        [sg.Button('Já possuo conta'), sg.Button('Cadastre-se agora')]
    ]
    return sg.Window('Atendimento', layout=layout, finalize=True)

def janela_login(): 
    sg.theme('Material1')

    layout = [
        [sg.Text('CPF', size=(7,1)), sg.Input(key='cpf', size=(26,1))],
        [sg.Text('Senha', size=(7,1)), sg.Input(key='senha',password_char='*', size=(26,2))],
        [sg.Radio('Conta Corrente', "radio1", key='corrente1', default=True), 
         sg.Radio('Conta Poupança', "radio1", key='poupanca1', default=False)],
        [sg.Checkbox('Manter-me conectado')],
        [sg.Button('Entrar'), sg.Button('Voltar')]
]
    return sg.Window('Fazer Login', layout=layout, finalize=True)

def janela_cadastro():
    sg.theme('Material1')
    layout = [
        [sg.Text('Nome do Titular', size=(14,1)), sg.Input(key='titular', size=(30,2))],
        [sg.Text('Senha', size=(14,1)), sg.Input(key='senha2',password_char='*', size=(30,2))],
        [sg.Text('CPF', size=(14,1)), sg.Input(key='cpf2', size=(30,2))],
        [sg.Text('Tipo de conta:'), sg.Radio('Conta Corrente', "radio1", key='corrente2', default=True), 
         sg.Radio('Conta Poupança', "radio1", key='poupanca2', default=False)],
        [sg.Button('Cadastrar'), sg.Button('Voltar')]
]
    return sg.Window('Criar conta', layout=layout, finalize=True)

def janela_usuario():
    sg.theme('Reddit')
    c = consult(values['cpf'], 'contacorrente')
    p = consult(values['cpf'], 'contapoupanca')

    if values['corrente1'] == True:
        layout = [
            [sg.Text('Conta Corrente', size=(27,1), font='Roboto')],
            [sg.Text()],
            [sg.Text('Titular: ', size=(7,1)), sg.Text(f'{c[1]}', size=(21,1))],
            [sg.Text('Conta: ', size=(7,1)), sg.Text(f'{c[0]}', size=(21,1))],
            [sg.Text('Saldo: ', size=(7,1)), sg.Text(f'{c[2]}', size=(21,1))],
            [sg.Button('Depositar', size=(10,2)), sg.Button('Sacar', size=(10,2)), sg.Button('Tirar Extrato', size=(10,2))],
            [sg.Button('Sair')]
        ]
    if values['poupanca1'] == True:
        layout = [
            [sg.Text('Conta Poupança', size=(27,1), font='Roboto')],
            [sg.Text()],
            [sg.Text('Titular: ', size=(7,1)), sg.Text(f'{p[1]}', size=(21,1))],
            [sg.Text('Conta: ', size=(7,1)), sg.Text(f'{p[0]}', size=(21,1))],
            [sg.Text('Saldo: ', size=(7,1)), sg.Text(f'{p[2]}', size=(21,1))],
            [sg.Button('Depositar', size=(10,2)), sg.Button('Sacar', size=(10,2)), sg.Button('Tirar Extrato', size=(10,2))],
            [sg.Button('Sair')]
        ]
    return sg.Window('Área do usuário', layout=layout, finalize=True)

def janela_deposito():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Depositar (R$):', size=(20,1)), sg.Input(key='deposito', size=(20,2))],
        [sg.Button('Confirmar'), sg.Button('Voltar')]
]
    return sg.Window('Criar conta', layout=layout, finalize=True)

def janela_saque():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Sacar (R$):', size=(20,1)), sg.Input(key='saque', size=(20,2))],
        [sg.Button('Confirmar'), sg.Button('Voltar')]
]
    return sg.Window('Criar conta', layout=layout, finalize=True)

def janela_extrato():
    sg.theme('Reddit')

    font = ('Courier New', 16)
    temp = extrato(cpf1)
    # text = '\n'.join(temp(i) for i in range(65, 91))
    column = [
        [sg.Text(f'{temp}', font=font)] 
    ] 

    layout = [
        [sg.Column(column, size=(800, 300), scrollable=True, key = "Column")],
        [sg.Button('Voltar'), sg.Button('↑', key = "up"), sg.Button('↓', key = "down")],
    ]

    window = sg.Window('Extrato', layout, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "down":
            window['Column'].Widget.canvas.yview_moveto(1.0)
        elif event == "up":
            window['Column'].Widget.canvas.yview_moveto(0.0)
        

# Janelas iniciais

janela1, janela2, janela3, janela4, janela5, janela6, janela7 = janela_inicial(), None, None, None, None, None, None

# Eventos

while True:
    window, event, values = sg.read_all_windows()

    # Janela inicial
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Já possuo conta':
        janela1.hide()
        janela2 = janela_login()
    if window == janela1 and event == 'Cadastre-se agora':
        janela1.hide()
        janela3 = janela_cadastro()

    # Janela de Login
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if event == 'Entrar':
        if values['corrente1'] == True:
            radioLogin = True
            cpf1 = consult(values['cpf'], 'contacorrente')
            tipoc = 'contacorrente'
            if values['cpf'] == cpf1[4] and values['senha'] == cpf1[3]:
                janela2.hide()
                janela4 = janela_usuario()
            else:
                sg.popup('Usuário/Senha inválido(s)', title='Falha no Login', font='Verdana')
        elif values['poupanca1'] == True:
            radioLogin = False
            cpf1 = consult(values['cpf'], 'contapoupanca')
            tipoc = 'contapoupanca'
            if values['cpf'] == cpf1[5] and values['senha'] == cpf1[4]:
                janela2.hide()
                janela4 = janela_usuario()
            else:
                sg.popup('Usuário/Senha inválido(s)', title='Falha no Login', font='Verdana')
    
    # Janela de Cadastro
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()  
    if window == janela3 and event == 'Cadastrar':
        if Funcoes.validadeCPF(values['cpf2']) == True:
            if values['corrente2'] == True:
                radioCadastro = True
                if consult(values['cpf2'], 'contacorrente') == None:
                    CriaNovaConta(values['titular'], values['senha2'], values['cpf2'], 'contacorrente')
                    sg.popup('Cadastro realizado com sucesso', title='Operação bem-sucedida', font='Verdana')
                    janela3.hide()
                    janela2 = janela_login()
                else:
                    sg.popup('CPF já cadastrado!', title='Erro na operação', font='Verdana')
            if values['poupanca2'] == True:
                radioCadastro = False
                if consult(values['cpf2'], 'contapoupanca') == None:
                    CriaNovaConta(values['titular'], values['senha2'], values['cpf2'], 'contapoupanca')
                    sg.popup('Cadastro realizado com sucesso', title='Operação bem-sucedida', font='Verdana')
                    janela3.hide()
                    janela2 = janela_login()
                else:
                    sg.popup('CPF já cadastrado!', title='Erro na operação', font='Verdana')
    
    # Janela do usuário
    if window == janela4 and event == sg.WIN_CLOSED:
        break
    if window == janela4 and event == 'Sair':
        janela4.hide()
        janela2 = janela_login()
    if window == janela4 and event == 'Depositar':
        janela4.hide()
        janela5 = janela_deposito()
    if window == janela4 and event == 'Sacar':
        janela4.hide()
        janela6 = janela_saque()
    if window == janela4 and event == 'Tirar Extrato':
        janela4.hide()
        janela7 = janela_extrato()
            
    
    # Janela de depósito
    
    if window == janela5 and event == sg.WIN_CLOSED:
        break
    if window == janela5 and event == 'Voltar':
        janela5.hide()
        janela4.un_hide()
    if window == janela5 and event == 'Confirmar':
        if radioLogin == True:
            deposito(cpf1[4], values['deposito'], 'contacorrente')
            sg.popup('Depósito realizado com sucesso', title='Operação bem-sucedida', font='Verdana')
            janela5.hide()
            janela4.un_hide()
        if radioLogin == False:
            deposito(cpf1[5], values['deposito'], 'contapoupanca')
            sg.popup('Depósito realizado com sucesso', title='Operação bem-sucedida', font='Verdana')
            janela5.hide()
            janela4.un_hide()
    
    # Janela de saque

    if window == janela6 and event == sg.WIN_CLOSED:
        break
    if window == janela6 and event == 'Voltar':
        janela6.hide()
        janela4.un_hide()
    if window == janela6 and event == 'Confirmar':
        if radioLogin == True:
            print(type(cpf1[4]))
            saque(cpf1[4], values['saque'], 'contacorrente')
            print(type(cpf1[4]))
            sg.popup('Saque realizado com sucesso', title='Operação bem-sucedida', font='Verdana')
            janela5.hide()
            janela4.un_hide()
        if radioLogin == False:
            saque(cpf1[5], values['saque'], 'contapoupanca')
            sg.popup('Saque realizado com sucesso', title='Operação bem-sucedida', font='Verdana')
            janela5.hide()
            janela4.un_hide()

    # Janela de extrato

    # if window == janela7 and event == sg.WIN_CLOSED:
    #     break
    # if window == janela7 and event == 'Voltar':
    #     janela7.hide()
    #     janela4.un_hide()