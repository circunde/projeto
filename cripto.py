import random

caixacodigo = {'1':'qaz', '2':'wsx', '3':'edc', '4':'rfv', '5':'tgb', '6':'yhn', '7':'ujm', '8':'ik', '9':'ol', '0':'pç',
               '1#':'QAZ', '2#':'WSX', '3#':'EDC', '4#':'RFV', '5#':'TGB', '6#':'YHN', '7#':'UJM', '8#':'IK', '9#':'OL',
               '0#':'PÇ','1b':'á', '3b':'é','8b':'í', '9b':'ó', '7b': 'ú', '1B':'Á', '3B':'É', '8B':'Í', '9B':'Ó','7B': 'Ú',
               '1c':'â', '3c':'ê', '8c':'î', '9c':'ô', '7c':'û', '1C':'Â', '3C':'Ê','8C':'Î', '9C':'Ô','7C':'Û', '1d':'ã',
               '9d':'õ', '1D':'Ã', '9D':'Õ'}


class Criptografia(object):
    ''' *** codificar a mensagem ***
        *** descodificar a mensagem ***
        crio esse programa no intuito de formar minha propria criptografia para fins de uso proprio
        - tabela
        - informaçao recebida
        - informaçao convertida
        - diferentes formas de cripto
        - testes
        - ajustes
        - u-d-t-q-c-s-st-o-n-z
       '''

    def __init__(self):
        salvar = False
        self.entradaDaMsg = input('entrada de texto: ')
        self.comando = input('o que deve ser feito ? ')
        if self.comando == 'salvar':
            salvar = True
            if salvar == True:
                self.SalvarMsg()
            print('salvo !')

        elif self.comando == '1':
            self.Codificar()

        else:
            print('nada foi alterado')

    def SalvarMsg(self):
        self.arquivar = open('Msgs.txt', 'w')
        self.arquivar.write(self.entradaDaMsg)
        self.arquivar.write('\n')
        self.arquivar.close()

    def Codificar(self):
        valores = []
        LetrasEmOrdem = []

        for k, v in caixacodigo.items():
            for r in v:
                if r in self.entradaDaMsg:
                    LetrasEmOrdem.append(r)
                    LetrasEmOrdem.sort()
                    valores.append(k)
        print(LetrasEmOrdem)
        print(valores)





Criptografia()

'''        for k,v in caixacodigo.items():
            if v == self.entradaDaMsg:
                print(k)'''