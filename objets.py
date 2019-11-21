import copy


class Pelouse:
    def __init__(self, x, y):

        X, Y = int(x), int(y)
        assert X > 0 and Y > 0, "carte non valable"

        self.limX = int(x)
        self.limY = int(y)


class Tondeuse:
    # orientation[self.O][deplacement] donne le sens dans lequel doit s'orienter la tondeuse
    orientation = {'N':
                   {'G': 'W',
                    'D': 'E'},
                   'S':
                   {'G': 'E',
                    'D': 'W'},
                   'E':
                   {'G': 'N',
                    'D': 'S'},
                   'W':
                   {'G': 'S',
                    'D': 'N'}
                   }

    def __init__(self, pelouse, init_pos):

        X, Y, O = init_pos
        X, Y = int(X), int(Y)

        assert O in ['N', 'S', 'E', 'W'], "Orientation non valide"
        assert (0 < X < pelouse.limX) and (
            0 < Y < pelouse.limY), "Position non valable"

        self.limX = pelouse.limX
        self.limY = pelouse.limY
        self.X = X
        self.Y = Y
        self.O = O
        self.pelouse = pelouse

    def __str__(self):
        return f"{self.X}, {self.Y}, {self.O}"

    def __repr__(self):
        return f"{self.X}, {self.Y}, {self.O}"

    def copy(self):
        return copy.deepcopy(self)

    def can_move(self, deplacement):
        # verifier que le déplacement est possible
        assert deplacement in ['G', 'D', 'A'], "Déplacement non valide"
        tond_bis = self.copy()
        tond_bis.move(deplacement)
        return tond_bis.is_legit()

    def is_legit(self):
        return (0 <= self.X <= self.limX) and (0 <= self.Y <= self.limY)

    def move(self, deplacement):
        # effectue le movement
        if deplacement == 'G':
            self.O = Tondeuse.orientation[self.O]['G']

        if deplacement == 'D':
            self.O = Tondeuse.orientation[self.O]['D']

        if deplacement == 'A':

            if self.O == 'N':
                self.Y = self.Y + 1
            if self.O == 'S':
                self.Y = self.Y - 1
            if self.O == 'E':
                self.X = self.X + 1
            if self.O == 'W':
                self.X = self.X - 1

    def full_move(self, chemin):

        for indice, dep in enumerate(chemin):
            if (self.can_move(dep)):
                # print(dep)
                self.move(dep)
