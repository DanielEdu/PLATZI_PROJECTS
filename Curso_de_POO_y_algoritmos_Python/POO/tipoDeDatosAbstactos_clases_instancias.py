
class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, new_coordenada):
        x_diff = (self.x - new_coordenada.x)**2
        y_diff = (self.y - new_coordenada.x)**2

        return (x_diff + y_diff)**0.5


def run():
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 40)
    var = 55+1

    print(coord_1.distancia(coord_2))
    print(isinstance(var, Coordenada))  # consultar si un objeto es instancia de una clase



if __name__ == '__main__':
    run()

