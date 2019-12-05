import os
import pandas
from random import *

class Character(object):

    def __init__(self, nom, titre, force, vie):
        self.nom = nom
        self.titre = titre
        self.force = force
        self.vie = vie

    def fight(self, ennemy):
        global chars_comp
        en = ennemy.titre + ' ' + ennemy.nom
        sf = self.titre + ' ' + self.nom
        c1 = sf + ' a encore ' + str(self.vie) + ' points de vie.'
        c2 = en + ' a encore ' + str(ennemy.vie) + ' points de vie.'
        print('HA ! ', sf, ' s\'attaque à ', en, ' !')
        print('Il lui inflige ', self.force, ' points de dégats et en subi ', ennemy.force)
        self.vie -= ennemy.force
        ennemy.vie -= self.force
        if ennemy.vie > 0 and self.vie > 0:
            print(c1)
            print(c2)
        elif ennemy.vie <= 0 and self.vie > 0:
            print(c1)
            print(en, ' retourne dans sa pokéball ! Aurevoir ', en, ' !')
            chars_comp.remove(ennemy)
        elif (ennemy.vie and self.vie) <= 0:
            print('Doublette ! ', en, ' et ', sf, ' se sont entretués !')
            chars_comp.remove(ennemy)
            chars_comp.remove(self)
        else:
            print(c2)
            print(sf, ' retourne dans sa pokéball ! Aurevoir ', sf, ' !')
            chars_comp.remove(self)

titres = ['Princesse', 'Dragon', 'Tyran', 'Dictateur', 'Leader', 'Sa majesté', 'Chef', 'Sauvage', 'Roi de la jungle', 'Chasseur', 'Kangourou']
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
    chars_comp.append(Character(i, choice(titres), choice(forces), choice(vies)))

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