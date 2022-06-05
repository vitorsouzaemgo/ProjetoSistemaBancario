import PySimpleGUI as sg
import Funcoes
from bank_date import *

# Layout

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
    layout = [
        [sg.Button('Depositar', size=(10,2)), sg.Button('Sacar', size=(10,2)), sg.Button('Tirar Extrato', size=(10,2))],
        [sg.Button('Sair')]
    ]
    return sg.Window('Área do usuário', layout=layout, finalize=True)

# Janelas iniciais

janela1, janela2, janela3, janela4 = janela_inicial(), None, None, None

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
        cpf1 = consult(values['cpf'])
        print(cpf1)
        if values['cpf'] == cpf1[4] and values['senha'] == cpf1[3]:
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
    if window == janela3 and event == 'Solicitar':
        if Funcoes.validadeCPF(values['cpf2']) == True:
            sg.popup('Solicitação realizada com sucesso', title='Solicitação bem-sucedida', font='Verdana')
            janela3.hide()
            janela2 = janela_login()
    
    # Janela do usuário
    if window == janela4 and event == sg.WIN_CLOSED:
        break
    if window == janela4 and event == 'Sair':
        janela4.hide()
        janela2 = janela_login()
