import random

caixacodigo = {'1':'qaz', '2':'wsx', '3':'edc', '4':'rfv', '5':'tgb', '6':'yhn', '7':'ujm', '8':'ik', '9':'ol', '0':'p�',
               '1#':'QAZ', '2#':'WSX', '3#':'EDC', '4#':'RFV', '5#':'TGB', '6#':'YHN', '7#':'UJM', '8#':'IK', '9#':'OL',
               '0#':'P�','1b':'�', '3b':'�','8b':'�', '9b':'�', '7b': '�', '1B':'�', '3B':'�', '8B':'�', '9B':'�','7B': '�',
               '1c':'�', '3c':'�', '8c':'�', '9c':'�', '7c':'�', '1C':'�', '3C':'�','8C':'�', '9C':'�','7C':'�', '1d':'�',
               '9d':'�', '1D':'�', '9D':'�'}


class Criptografia(object):
    ''' *** codificar a mensagem ***
        *** descodificar a mensagem ***
        crio esse programa no intuito de formar minha propria criptografia para fins de uso proprio
        - tabela
        - informa�ao recebida
        - informa�ao convertida
        - diferentes formas de cripto
        - testes
        - ajustes
        - u-d-t-q-c-s-st-o-n-z
        - �-�-�-�-� - �-�-�-�-� - �-�
        - �-�-�-�-� - �-�-�-�-� - �-�'''

    def __init__(self):
        salvar = False
        self.entradaDaMsg = input('entrada de texto: ')
        self.comando = input('o que deve ser feito ? ')
        if self.comando == 'salvar':
            salvar = True
            if salvar == True:
                self.SalvarMsg()
            print('salvo !')
        elif self.comando == 'codificar':
            self.Codificar()

        else:
            print('o texto ser� codificado')

    def SalvarMsg(self):
        self.arquivar = open('Msgs.txt', 'w')
        self.arquivar.write(self.entradaDaMsg)
        self.arquivar.write('\n')
        self.arquivar.close()

    def Codificar(self):
        valores = [caixacodigo.values()]

        for letras in self.entradaDaMsg:
            if letras in valores:
                return print(caixacodigo.keys())
            else:
                return 0