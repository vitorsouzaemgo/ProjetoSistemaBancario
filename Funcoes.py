import PySimpleGUI as sg

def validadeCPF(cpf):
    if len(cpf) != 11:
        sg.popup('Tamanho de CPF inválido', title='Falha no Cadastro')
        print(len(cpf))
    elif len(cpf)==11:
        temp = [int(cpf[0]), int(cpf[1]), int(cpf[2]), int(cpf[3]), int(cpf[4]), int(cpf[5]), int(cpf[6]), int(cpf[7]), int(cpf[8])]
        soma1 = (temp[0]*10) + (temp[1]*9) + (temp[2]*8) + (temp[3]*7) + (temp[4]*6) + (temp[5]*5) + (temp[6]*4) + (temp[7]*3) + (temp[8]*2)
        if (11-(soma1%11)) >= 10:
            resultado1 = 0
        else:
            resultado1 = (11-(soma1%11))

        print((int(cpf[0]*10)),(int(cpf[1]*9)), (int(cpf[2]*8)), (int(cpf[3]*7)), (int(cpf[4]*6)), (int(cpf[5]*5)), (int(cpf[6]*4)), (int(cpf[7]*3)), (int(cpf[8]*2)), soma1, resultado1)

        if resultado1 != cpf[9]:
            sg.popup('CPF inválido', title='Falha no Cadastro')
        else:
            soma2 = (int(cpf[0])*11) + (int(cpf[1])*10) + (int(cpf[2])*9) + (int(cpf[3])*8) + (int(cpf[4])*7) + (int(cpf[5])*6) + (int(cpf[6])*5) + (int(cpf[7])*4) + (int(cpf[8])*3) + (int(cpf[9])*2)
            if (11-(soma2%11)) >= 10:
                resultado2 = 0
            else:
                resultado2 = (11-(soma2%11))

            """ print(soma2, resultado2) """

            if resultado2 != cpf[10]:
                sg.popup('CPF inválido', title='Falha no Cadastro')