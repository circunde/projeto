import random


'''crio esse programa no intuito de formar minha propria criptografia para fins de uso proprio
- tabela 
- informaçao recebida
- informaçao convertida 
- diferentes formas de cripto
- testes
- ajustes
- u-d-t-q-c-s-st-o-n-z 
- á-é-í-ó-ú - â-ê-î-ô-û - ã-õ
- Á-É-Í-Ó-Ú - Â-Ê-Î-Ô-Û - Ã-Õ
                                                                                  '''

caixacodigo = {'1':'qaz', '2':'wsx', '3':'edc', '4':'rfv', '5':'tgb', '6':'yhn', '7':'ujm', '8':'ik', '9':'ol', '0':'pç',
               '1#':'QAZ', '2#':'WSX', '3#':'EDC', '4#':'RFV', '5#':'TGB', '6#':'YHN', '7#':'UJM', '8#':'IK', '9#':'OL',
               '0#':'PÇ','1b':'á', '3b':'é','8b':'í', '9b':'ó', '7b': 'ú', '1B':'Á', '3B', '8B', '9B', '7B','1c', '3c', '8c', '9c', '7c', '1C', '3C',
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
caixacodigo[9] = 'pç'
caixacodigo[10] = 'QAZ'
caixacodigo[11] = 'WSX'
caixacodigo[12] = 'EDC'
caixacodigo[13] = 'RFV'
caixacodigo[14] = 'TGB'
caixacodigo[15] = 'YHN'
caixacodigo[16] = 'UJM'
caixacodigo[17] = 'IK'
caixacodigo[18] = 'OL'
caixacodigo[19] = 'PÇ'
caixacodigo[20] = 'á'
caixacodigo[21] = 'é'
caixacodigo[22] = 'í'
caixacodigo[23] = 'ó'
caixacodigo[24] = 'ú'
caixacodigo[25] = 'Á'
caixacodigo[26] = 'É'
caixacodigo[27] = 'Í'
caixacodigo[28] = 'Ó'
caixacodigo[29] = 'Ú'
caixacodigo[30] = 'â'
caixacodigo[31] = 'ê'
caixacodigo[32] = 'î'
caixacodigo[33] = 'ô'
caixacodigo[34] = 'û'
caixacodigo[35] = 'Â'
caixacodigo[36] = 'Ê'
caixacodigo[37] = 'Î'
caixacodigo[38] = 'Ô'
caixacodigo[39] = 'Û'
caixacodigo[40] = 'ã'
caixacodigo[41] = 'õ'
caixacodigo[42] = 'Ã'
caixacodigo[43] = 'Õ'

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
            return print('o texto será codificado')

    def SalvarMsg(self):
        self.arquivar = open('Msgs.txt', 'w')
        self.arquivar.write(self.entradaDaMsg)
        self.arquivar.write('\n')
        self.arquivar.close()

    def Codificar(self):
        for var in