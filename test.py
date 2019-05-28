import pickle


def Contas(usuario, passw):
    try:
        Users = pickle.load(open('test.pkl', 'rb'))
        print(Users)

        '''usr = usuario
        senha = passw


        if usr == '' and senha == '':
            Users.append('*')
        else:
            Users.append({usr: senha})'''

        pickle.dump(Users, open('test.pkl', 'wb'))
    except:
        Users = []
        print('recriando')
        pickle.dump(Users, open('test.pkl', 'wb'))
        # caixa.close()


Contas('', '')
