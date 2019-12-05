import os
import pandas
from random import *

# On définit une classe (un modèle), sur laquelle construire nos instances
class Character(object):

    # On utilise donc une méthode, qui est similaire à une fonction mais est contenue au sein d'une classe. Ici la méthode spéciale (spéciale car on y met __ de part et d'autre) init est appelée un constructeur, c'est la méthode qui sera appelée a chaque initialisation d'une instance de cette classe
    def __init__(self, nom, race, force, vie):
        # C'est au sein de ce constructeur que l'on va définir nos attributs. Les attributs sont en quelques sortes des variables communes a toute les instances d'une même classe. On peut en passer en parametre pour definir ces attributs à la création de l'instance ou bien ..
        self.nom = nom
        self._race = race
        self.force = force
        self.vie = vie
        # .. on peut aussi definir une valeur non passée en parametre qui sera 'par default' la même à toutes les instances
        self.age = 24
        print('Un nouveau personnage est né !')
    
    # Exemple d'encapsulation pour l'accès à l'attribut race
    def _get_race(self):
        print(self.nom, ' est de la race des ', self._race)
        pass
    
    # On donne l'instruction que l'attribut race est une propriété et prends des encapsulations en paramètre (içi uniquement l'accès)
    race = property(_get_race)

    # Içi, nous allons définir notre premiere méthode 'maison'. Nous voulons se faire battre deux personnages (donc deux instances) entre elles, et changer certaines valeurs (points de vie) à l'issue du combat
    # Nous allons donc passer le parametre 'self' qui cible l'instance sur laquelle on applique la methode, et un deuxieme parametre qui sera l'adversaire affronté
    def fight(self, ennemy):
        global chars_comp
        print('HA ! ', self.nom, ' s\'attaque à ', ennemy.nom, ' !')
        print('Il lui inflige ', self.force, ' points de dégats et en subi ', ennemy.force)
        # Les deux personnages ont subi des dégats. On va donc modifier la valeur vie de chacune de ces instances afin de le prendre en compte
        self.vie -= ennemy.force
        ennemy.vie -= self.force
        # Conditions pour verifier si le personnage est encore en vie
        if ennemy.vie > 0 and self.vie > 0:
            print(self.nom, ' a encore ', self.vie, ' points de vie.')
            print(ennemy.nom, ' a encore ', ennemy.vie, ' points de vie.')
        elif ennemy.vie <= 0 and self.vie > 0:
            print(self.nom, ' a encore ', self.vie, ' points de vie.')
            print(ennemy.nom, ' retourne dans sa pokéball ! Aurevoir ', ennemy.nom, ' !')
            chars_comp.remove(ennemy)
        elif (ennemy.vie and self.vie) <= 0:
            print('Doublette ! ', ennemy.nom, ' et ', self.nom, ' se sont entretués !')
            chars_comp.remove(ennemy)
            chars_comp.remove(self)
        else:
            print(ennemy.nom, ' a encore ', ennemy.vie, ' points de vie.')
            print(self.nom, ' retourne dans sa pokéball ! Aurevoir ', self.nom, ' !')
            chars_comp.remove(self)

"""
# On crée notre premiere instance, pour cela on fait appelle a la classe sur laquelle se construire et on passe les parametres nécéssaires entre parenthèses
p1 = Character('Johnny', 'Gobelin', 5, 30)
p2 = Character('Mickey', 'Souris maléfique', 10, 10)
print(p1.vie)
# On demande au script d'afficher la vie de p1
>> 30
# On peut aussi bien changer cette valeur
p1.vie = 50
print(p1.vie)
>> 50
# Maintenant, Mickey et Johnny vont se battre ! Mickey va donc attaquer Johnny
p2.fight(p1)
>> HA ! Mickey s'attaque à Johnny !
>> Il lui inflige 10 points de dégats et en subi 5
>> Mickey a encore 5 points de vie.
>> Johnny a encore 40 points de vie.
"""


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
            for i in chars_comp:
                print(i.nom)
            if len(chars_comp) ==0:
                print('Personne n\'a gagné :(')
            main()
        else:
            print(chars_comp[0].nom, ' a gagné ! BRAVOOOOOOOOOOO !')

main()