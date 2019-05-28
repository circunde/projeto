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
        self.letras = ('Arial', '14', 'bold')
        self.letras2 = ('Verdana', '10', 'bold')
        # informação do programa;
        self.inf1 = Label(janela, text='Gerenciador de senhas', width='20', fg='white', bg='#3CB371', font=self.letras)
        self.inf1.pack()

        # imagem
        self.img = PhotoImage(file='matrix.gif')
        w = Label(janela, image=self.img, bd='0')
        w.imagem = self.img
        w.pack()

        # entrada de usuario;
        self.entU = Entry(janela, bd='4', font=self.letras, justify=CENTER, width='15', bg='#228B22')
        self.entU.pack()

        # entrada de senha;
        self.entS = Entry(janela, show='*', font=self.letras, bd='4', justify=CENTER, width='15', bg='#228B22')
        self.entS.pack()

        # ação de salvar o usuario e senha;
        self.botS = Button(janela, text='Salvar', command=self.Criar_User, font=self.letras2, width='10',
                           bg='#008000', )
        self.botV = Button(janela, text='Visualizar', command=self.Visualizar, font=self.letras2, width='10',
                           bg='#008000')
        self.botG = Button(janela, text='Gerar senha', command=self.Gerar, font=self.letras2, width='10',
                           bg='#008000', )
        self.botS.pack(side=LEFT)
        self.botV.pack(side=LEFT)
        self.botG.pack(side=LEFT)

        # informação final;
        self.inf2 = Label(janela2, text='', bg='black', font=('Verdana', '10', 'italic bold'))
        self.inf2.pack(side=LEFT)

        # database
        self.database = pickle.load(open('test.pkl', 'rb'))
        print(self.database)

    # função para salvar usuário e senha;
    def Criar_User(self):
        caixaU = self.entU.get()
        caixaS = self.entS.get()
        self.database.append({caixaU: caixaS})
        import test
        #test.Contas(caixaU,caixaS)
        pickle.dump(self.database,open('test.pkl','wb'))


    # visualizar os Usuarios e senha;
    def Visualizar(self):
        user = self.entU.get()
        if user == 'r4':

            self.MSG(self.database)
            self.inf2['bg'] = '#87CEEB'
        else:
            self.inf2['text'] = self.MSG('Chave necessária')
        #self.inf2['text'] = 'test'

    # mensagem
    def MSG(self, msg, cor='red', Fundo='#87CEEB'):
        self.inf2['text'] = msg
        self.inf2['fg'] = cor

    # gerar senha para Usuário
    def Gerar(self):
        pass


tela = Tk()
janela = Frame(tela)
janela.pack()
janela2 = Frame(tela)
janela2.pack()
tela['bg'] = 'black'
janela['bg'] = 'black'
Formulario(janela)
tela.title('Gerenciador de Senhas')
tela.geometry('500x320')

mainloop()

'''NÃO MEXER'''