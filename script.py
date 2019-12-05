import os
import pandas
from random import *

class Character(object):

    def __init__(self, nom, race, force, vie):
        self.nom = nom
        self._race = race
        self.force = force
        self.vie = vie
        print('Un nouveau personnage est né !')
    
    def _get_race(self):
        print(self.nom, ' est de la race des ', self._race)
        pass
    
    race = property(_get_race)

    def fight(self, ennemy):
        global chars_comp
        c1 = print(self.nom, ' a encore ', self.vie, ' points de vie.')
        c2 = print(ennemy.nom, ' a encore ', ennemy.vie, ' points de vie.')
        print('HA ! ', self.nom, ' s\'attaque à ', ennemy.nom, ' !')
        print('Il lui inflige ', self.force, ' points de dégats et en subi ', ennemy.force)
        self.vie -= ennemy.force
        ennemy.vie -= self.force
        if ennemy.vie > 0 and self.vie > 0:
            c1
            c2
        elif ennemy.vie <= 0 and self.vie > 0:
            c1
            print(ennemy.nom, ' retourne dans sa pokéball ! Aurevoir ', ennemy.nom, ' !')
            chars_comp.remove(ennemy)
        elif (ennemy.vie and self.vie) <= 0:
            print('Doublette ! ', ennemy.nom, ' et ', self.nom, ' se sont entretués !')
            chars_comp.remove(ennemy)
            chars_comp.remove(self)
        else:
            c2
            print(self.nom, ' retourne dans sa pokéball ! Aurevoir ', self.nom, ' !')
            chars_comp.remove(self)

races = ['orc', 'poulet', 'tortue']
forces = []
for i in range(10, 16):
    forces.append(i)
vies = []
for i in range(80, 101):
    vies.append(i)

f = pandas.read_csv('DataJungleFighterz.csv')
f = f.values.tolist()

new_f = []
for i in f:
    new_f = new_f + i

chars_comp = []
for i in new_f:
    chars_comp.append(Character(i, choice(races), choice(forces), choice(vies)))

def main():
    global chars_comp
    continue_game = input('Appuyez sur entrée pour le combat suivant ou entrez une touche auparavant pour quitter')
    if continue_game != '':
        print('Aurevoir, à bientôt !')
    else:
        if len(chars_comp) > 2:
            char_a = choice(chars_comp)
            chars_comp.remove(char_a)
            char_b = choice(chars_comp)
            chars_comp.append(char_a)
            char_a.fight(char_b)
            print("\n", len(chars_comp), "Fighterz En Vie:\n")
            chars_comp = sorted(chars_comp, key= lambda char: char.vie, reverse=True)
            for i in chars_comp:
                print(i.nom, ' avec ', i.vie, ' points de vie.')
            if len(chars_comp) ==0:
                print('Personne n\'a gagné :(')
            main()
        else:
            print(chars_comp[0].nom, ' a gagné ! BRAVOOOOOOOOOOO !')

main()