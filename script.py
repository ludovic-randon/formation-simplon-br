import os
import pandas
from random import *

class Character(object):
    
    randomInit = ["descend de son carrosse", "est sortie de sa capsule", "sort de terre", "tombe du ciel",  "est envoyé par les dieux", "arrive en moonwalk", "s'est perdu #Denis", "prend les armes", "déménage", "enleve sa cape d'invisibilité", "recherche à manger", "pose son café", "releve ses manches", "se réveille", "est push sur le terrain", "débarque à dos de licorne", "veut tout casser", "est pret à en decoudre", "a la grippe", "est pret pour le stand up", "rassemble ses chakras", "sort son chéquier"]
        
    def __init__(self, nom, titre, arme, min_dmg, max_dmg, percent, vie):
        self.nom = nom
        self.titre = titre
        self.arme = arme
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.percent = percent
        self.vie = vie
        print(self.titre, self.nom, choice(Character.randomInit), 'avec', self.arme)

    def fight(self, ennemy):
        global chars_comp
        en = ennemy.titre + ' ' + ennemy.nom
        sf = self.titre + ' ' + self.nom
        print('HA ! ', sf, ' s\'attaque à ', en, ' !')
        en_dmg = randrange(ennemy.min_dmg, ennemy.max_dmg)
        sf_dmg = randrange(self.min_dmg, self.max_dmg)
        print('Il lui inflige ', sf_dmg, ' points de dégats et en subi ', en_dmg)
        self.vie -= en_dmg
        ennemy.vie -= sf_dmg
        
        if  randrange(0,100) < 10:
            print("\nBOUM ! Samba Sauvage apparait et lance GAOUUU il inflige 20 de degat à ", en , " et ", sf, "\n")
            self.vie -= 20
            ennemy.vie -= 20
        
        if  randrange(0,100) < 10:
            print("\nBOUM ! Rafik apparait et vous piege dans algorithme et vous force a vous rebattre\n")
            
            rafikNb = randrange(1,5)
            print(rafikNb, "fois !!\n")
            i = 0
            while i < rafikNb:
                print(sf, ' s\'attaque à nouveau à ', en, ' !')
                print('Il lui inflige ', sf_dmg, ' points de dégats et en subi ', en_dmg, "\n")
                self.vie -= en_dmg
                ennemy.vie -= sf_dmg
                i += 1
        
        c1 = sf + ' a encore ' + str(self.vie) + ' points de vie.'
        c2 = en + ' a encore ' + str(ennemy.vie) + ' points de vie.'
        
                
        if randrange(0,100) < 5:
            print("\nBOUM ! Samba Sauvage apparait et lance FRAPPE LOURDE il detruit ", en , " et ", sf, "\n")
            chars_comp.remove(ennemy)
            chars_comp.remove(self)
        elif ennemy.vie > 0 and self.vie > 0:
            print(c1)
            print(c2)
        elif ennemy.vie <= 0 and self.vie > 0:
            print(c1)
            print(en, ' retourne dans sa pokéball ! Aurevoir ', en, ' !')
            chars_comp.remove(ennemy)
        elif ennemy.vie <= 0 and self.vie <= 0:
            print('Doublette ! ', en, ' et ', sf, ' se sont entretués !')
            chars_comp.remove(ennemy)
            chars_comp.remove(self)
        else:
            print(c2)
            print(sf, ' retourne dans sa pokéball ! Aurevoir ', sf, ' !')
            chars_comp.remove(self)


class Arme:

    def __init__(self, nom, damage_min, damage_max, percent):
        self.nom = nom
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.percent = percent


weapon_list = []
weapon_list.append(Arme('un pistolet', 10, 14, 80))
weapon_list.append(Arme('un couteau', 5, 6, 95))
weapon_list.append(Arme('un M16', 18, 26, 60))
test_un = choice(weapon_list)
print(test_un.nom, ' ', test_un.damage_min, ' ', test_un.damage_max)

titres = ['Princesse', 'Petite fée', 'Vagabond', 'Voleur', 'Génie', 'Collabo', 'Dragon', 'Tyran', 'Dictateur', 'Leader', 'Sa majesté', 'Chef', 'Sauvage', 'Roi de la jungle', 'Chasseur', 'Kangourou']

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
    weap = choice(weapon_list)
    chars_comp.append(Character(i, choice(titres), weap.nom, weap.damage_min, weap.damage_max, weap.percent, choice(vies)))

def main():
    global chars_comp
    continue_game = input('\nAppuyez sur entrée pour le combat suivant ou entrez une touche auparavant pour quitter\n')
    if continue_game != '':
        print('Aurevoir, à bientôt !')
    else:
        if len(chars_comp) > 1:
            char_a = choice(chars_comp)
            chars_comp.remove(char_a)
            char_b = choice(chars_comp)
            chars_comp.append(char_a)
            char_a.fight(char_b)
            print("\n", len(chars_comp), "Fighterz En Vie:\n")
            chars_comp = sorted(chars_comp, key= lambda char: char.vie, reverse=True)
            for i in chars_comp:
                print(i.titre, i.nom, ' avec ', i.vie, ' points de vie.')
            if len(chars_comp) == 0:
                print('Personne n\'a gagné :(')
                pass
            elif len(chars_comp) == 1:
                print('\n', chars_comp[0].titre, ' ', chars_comp[0].nom, ' a gagné ! BRAVOOOOOOOOOOO !')
                pass
            else:
                main()

main()