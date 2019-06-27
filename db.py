import pickle


def Contas():
    try:
        Users = pickle.load(open('dbr.pkl', 'rb'))
        print(Users)
        pickle.dump(Users, open('dbr.pkl', 'wb'))
    except:
        Users = []
        print('recriando')
        pickle.dump(Users, open('dbr.pkl', 'wb'))



Contas()
