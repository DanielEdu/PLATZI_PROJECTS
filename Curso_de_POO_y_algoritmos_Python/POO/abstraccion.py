
class Lavadora:
    
    def __init__(self):
        pass
    
    #creando interfaz lavar para el usuario de la clase Lavadora
    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print(f'aniadiendo jabon')

    def _lavar(self):
        print(f'Lavando ropa')

    def _centrifugar(self):
        print(f'centrifugando ropa')



def run():
    lavadora = Lavadora()

    lavadora.lavar()


if __name__ == '__main__':
    run()
