import pickle
from tkinter import *
#from tkinter import messagebox

# classe de formulario para senhas
'''
- titulo
- entrada usuario
- entrada senha

'''


# #4169E1
# #696969

class Formulario(object):
    """esse programa será um formulario para as futuras senhas e usuarios """

    def __init__(self, janela):
        self.letras = ('Arial', '14')
        self.letras2 = ('Verdana', '10', 'bold')
        self.letras3 = ('Arial', '18')

        # informação do programa;
        self.inf1 = Label(janela, text='Gerenciador de senhas', width='20', fg='white', bg='#3CB371', font=self.letras)
        self.inf1.pack()

        # imagem
        self.img = PhotoImage(file='matrix.gif')
        w = Label(janela, image=self.img, bd='0')
        w.imagem = self.img
        w.pack()

        # entrada de usuario;
        self.entU = Entry(janela, bd='4', font=self.letras, justify=CENTER, width='15', bg='#8FBC8F')
        self.entU.pack()

        self.infU = Label(janela, text='Adicione Usuário ou informação principal', font=self.letras, bg='black',
                          fg='white')
        self.infU.pack()

        # entrada de senha;
        self.entS = Entry(janela, show='*', font=self.letras, bd='4', justify=CENTER, width='15', bg='#8FBC8F')
        self.entS.pack()

        self.infS = Label(janela, text='senha', font=self.letras, bg='black', fg='white')
        self.infS.pack()

        # ação de salvar o usuario e senha;
        self.botS = Button(janela, text='Salvar', command=self.Criar_User, font=self.letras2, width='10',
                           bg='#008000',activebackground='white',fg='#8FBC8F' )
        self.botV = Button(janela, text='Visualizar', command=self.Visualizar, font=self.letras2, width='10',
                           bg='#008000',activebackground='white',fg='#8FBC8F' )
        self.botG = Button(janela, text='Gerar senha', command=self.Gerar, font=self.letras2, width='10',
                           bg='#008000',activebackground='white',fg='#8FBC8F' )
        self.botD = Button(janela,text='Deletar',font=self.letras2, width='10',bg='red',activebackground='black',
                           activeforeground='white',command=self.ApagarDados,fg='#8FBC8F')

        self.botS.pack(side=LEFT)
        self.botV.pack(side=LEFT)
        self.botG.pack(side=LEFT)
        self.botD.pack(side=LEFT)

        # informação final;
        self.inf2 = Label(janela2, text='', bg='black', font=('Verdana', '10', 'italic bold'),
                          anchor='n',wraplength='400')
        self.inf2.pack(side=LEFT)


        # database
        self.database = pickle.load(open('test.pkl', 'rb'))
        print(self.database)

    # função para salvar usuário e senha;
    def Criar_User(self):
        caixa = self.entU.get(), '-', self.entS.get()

        if len(self.entU.get()) == 0 or len(self.entS.get()) == 0:
            self.MSG('Não pode conter espaços vazios','red',('Arial','14'))

        if caixa in self.database:
            self.MSG('Usuário existente','red',('Arial','14'))


        elif caixa not in self.database:
            self.database.append(caixa)
            self.MSG('Usuário adicionado','red',('Arial','14'))
            pickle.dump(self.database, open('test.pkl', 'wb'))

    # visualizar os Usuarios e senha;
    def Visualizar(self):
        user = self.entU.get()

        if user == '41796':
            self.MSG(self.database, 'red', ('Arial', '14', 'bold'))

            if len(self.database) == 0:
                self.inf2['text'] = self.MSG('não há dados')

            self.inf2['bg'] = '#000000'
        else:
            self.inf2['text'] = self.MSG('Chave necessária')

    # mensagem
    def MSG(self, msg, cor='red', fonte=('Arial','16','bold')):
        self.inf2['text'] = msg
        self.inf2['fg'] = cor
        self.inf2['font'] = fonte

    # gerar senha para Usuário
    def Gerar(self):
        import random

        gerador = 'ABCDEFGHIJLKMNOPQRSTUVWXYZabcdefghijlkmnopqrstuvwxyz1234567890@#$-_'
        box = []

        for i in range(9):
            box.append(random.choice(gerador))

        self.inf2['height'] = '50'
        self.inf2['font'] = self.letras
        self.MSG(box, 'green')


    def ApagarDados(self):
        caixa = self.entU.get(), '-', self.entS.get()
        user = self.entU.get()

        if caixa not in self.database:
            self.MSG('dados inexistentes')
            if user == '01019':
                self.database.clear()
                pickle.dump(self.database, open('test.pkl', 'wb'))
                self.MSG('lista apagada')
        else:
            self.database.remove(caixa)
            self.MSG('apagado com sucesso')
            pickle.dump(self.database, open('test.pkl','wb'))
        print(self.database)


tela = Tk()
janela = Frame(tela)
janela.pack()
janela2 = Frame(tela)
janela2.pack()
tela['bg'] = 'black'
janela['bg'] = 'black'
Formulario(janela)
tela.title('Gerenciador de Senhas')
tela.geometry('500x420')

mainloop()
