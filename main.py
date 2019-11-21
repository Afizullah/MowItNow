from objets import Tondeuse, Pelouse
import sys


def parse_lines(lines):
    """
    recueil la position initiale et le chemin à parcourir de la tondeuse
    """
    pos_init, chemin = lines[:2]
    pos_init = pos_init.split()

    return pos_init, chemin, lines[2:]


def main():

    # Lit le fichier d'entrée
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    num_tondeuse = 0
    # limite de la carte
    lim = lines[0].split()
    lines = lines[1:]

    pelouse = Pelouse(*lim)
    # liste des tondeuses
    tonds = []

    while(len(lines) > 1):

        num_tondeuse += 1
        pos_init, chemin, lines = parse_lines(lines)

        print(
            f"limite carte = {lim}, position initiale = {pos_init}, chemin = {chemin}, tondeuse n°{num_tondeuse}")

        tond = Tondeuse(pelouse, pos_init)
        tond.full_move(chemin)

        print(f"Tondeuse {num_tondeuse} : {tond.X} { tond.Y} {tond.O}")

        tonds.append(tond)


if __name__ == "__main__":
    main()
