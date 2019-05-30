import pickle


def Contas():
    try:
        Users = pickle.load(open('test.pkl', 'rb'))
        print(Users)
        pickle.dump(Users, open('test.pkl', 'wb'))
    except:
        Users = []
        print('recriando')
        pickle.dump(Users, open('test.pkl', 'wb'))



Contas()
