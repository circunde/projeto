import random


'''crio esse programa no intuito de formar minha propria criptografia para fins de uso proprio
- tabela 
- informa�ao recebida
- informa�ao convertida 
- diferentes formas de cripto
- testes
- ajustes
- u-d-t-q-c-s-st-o-n-z 
- �-�-�-�-� - �-�-�-�-� - �-�
- �-�-�-�-� - �-�-�-�-� - �-�
                                                                                  '''

caixacodigo = {'1':'qaz', '2':'wsx', '3':'edc', '4':'rfv', '5':'tgb', '6':'yhn', '7':'ujm', '8':'ik', '9':'ol', '0':'p�',
               '1#':'QAZ', '2#':'WSX', '3#':'EDC', '4#':'RFV', '5#':'TGB', '6#':'YHN', '7#':'UJM', '8#':'IK', '9#':'OL',
               '0#':'P�','1b':'�', '3b':'�','8b':'�', '9b':'�', '7b': '�', '1B':'�', '3B', '8B', '9B', '7B','1c', '3c', '8c', '9c', '7c', '1C', '3C',
               '8C', '9C','7C', '1d', '9d', '1D', '9D'}
caixacodigo[0] = 'qaz'
caixacodigo[1] = 'wsx'
caixacodigo[2] = 'edc'
caixacodigo[3] = 'rfv'
caixacodigo[4] = 'tgb'
caixacodigo[5] = 'yhn'
caixacodigo[6] = 'ujm'
caixacodigo[7] = 'ik'
caixacodigo[8] = 'ol'
caixacodigo[9] = 'p�'
caixacodigo[10] = 'QAZ'
caixacodigo[11] = 'WSX'
caixacodigo[12] = 'EDC'
caixacodigo[13] = 'RFV'
caixacodigo[14] = 'TGB'
caixacodigo[15] = 'YHN'
caixacodigo[16] = 'UJM'
caixacodigo[17] = 'IK'
caixacodigo[18] = 'OL'
caixacodigo[19] = 'P�'
caixacodigo[20] = '�'
caixacodigo[21] = '�'
caixacodigo[22] = '�'
caixacodigo[23] = '�'
caixacodigo[24] = '�'
caixacodigo[25] = '�'
caixacodigo[26] = '�'
caixacodigo[27] = '�'
caixacodigo[28] = '�'
caixacodigo[29] = '�'
caixacodigo[30] = '�'
caixacodigo[31] = '�'
caixacodigo[32] = '�'
caixacodigo[33] = '�'
caixacodigo[34] = '�'
caixacodigo[35] = '�'
caixacodigo[36] = '�'
caixacodigo[37] = '�'
caixacodigo[38] = '�'
caixacodigo[39] = '�'
caixacodigo[40] = '�'
caixacodigo[41] = '�'
caixacodigo[42] = '�'
caixacodigo[43] = '�'

class Criptografia(object):
    ''' *** codificar a mensagem ***
        *** descodificar a mensagem ***'''

    def __init__(self):
        salvar = False
        self.entradaDaMsg = input('entrada de texto: ')
        if self.entradaDaMsg == 'salvar':
            salvar = True
            if salvar == True:
                return self.SalvarMsg
            print('salvo !')
        else:
            return print('o texto ser� codificado')

    def SalvarMsg(self):
        self.arquivar = open('Msgs.txt', 'w')
        self.arquivar.write(self.entradaDaMsg)
        self.arquivar.write('\n')
        self.arquivar.close()

    def Codificar(self):
        for var in