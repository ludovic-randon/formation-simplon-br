# Openclassroom cours python

## 1- Perfectionnez vous en Python

### Aa- Téléchargements des ressources nécéssaires au cours
Cours et ressources [içi](https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4463200-organisez-un-script)
- La liste détaillée de nos députés (csv)
- Les comptes rendus des débats publics depuis 2013 (xml)

---

### Ab- Organisez un script
- Chemin + encodage à chaque script:
    ```
    #! usr/bin/env python3
    #coding: utf-8
    ```
- Fonction pour script main ou module :
    ```
    #Nous allons créer une encapsulation, pour que la fonction main ne s'execute que 
    si le fichier est utilisé comme script principal et non pas importé:

    def main():
        pass

    if __name__ == "__main__":
        main()
    ```

---

### Ac- Travaillez dans un environnement virtuel
- Environnement virtuel expliqué en dossier; Dossier dans lequel nous pourrons utilisé les mêmes ou differentes versions de librairies, de logiciels (ex: Python 3.6.2 sur l'ordinateur physique, mais Python 3.2.1 sur le dossier ou est installé l'environnement virtuel)

    ```
    pip install virtualenv
    ```
    1. Puis, nous allons build l'environnement virtuel:
        ```
        virtualenv -p python3 env
        ```
        'env' Sera le nom du dossier contenant l'environnement virtuel.
    2. Enfin, on active l'environnement virtuel:
        ```
        source env/bin/activate
        ```
        Doit alors s'afficher devant le root et le path :
            ```
            (env) root@root:~$ 
            ```
        '(env)' devant le root nous indique que nous sommes bien dans l'environnement virtuel activé nommé 'env'
    3. Si l'on veut désactiver celui-ci il suffit de taper :
        ```
        deactivate
        ```
- Pour ignorer les fichiers a utiliser avec git de l'environnement virtuel, nous allons utiliser un .gitignore:
    1. On créé tout d'abord à la racine le fichier .gitignore
    2. Dans ce fichier nous indiquons les dossiers et fichiers à ignorer par git (içi, 'env/')

- Nous créons un fichier de dépendance, par bonne pratique, nommé requirements.txt et listant les dépendances utilisées pour rendre la recherche de librairies utilisées moins fastidieuse
    1. Création du fichier dont la syntaxe interne est la suivante:
        ```
        librairie_une==version
        librairie_deux==version
        librairie_trois==version
        ```
    2. Pour qu'un utilisateur installe les librairies nécéssaires via ce fichier, il lui faudra utiliser la commande suivante :
        ```
        pip install -r requirements.txt
        ```

### Ad- Organisez un projet en modules

(current_dir = os.path.dirname(__file__);par_dir = os.path.abspath(os.pardir))

- On créé un dossier nommé data qui accueillera nos fichiers (csv et xml içi)
- On créé un fichier pour chaque type de fichier que l'on traitera (csv xml), ce sera nos modules.
    ```
    touch csv_analysis.py
    touch xml_analysis.py
    ```
- Içi, pour lire nos fichiers on doit se déplacer dans les répertoires
    1. On importe tout d'abord la librairie 'os'
        ```
        import os
        ```
    2. On défini une fonction main comme vu précédemment
    3. On ouvre le fichier csv ou xml avec open
        ```
        with open(path_to_file), 'r') as file:
        ```
    4. Placer les deux fichiers dans une dossier à la racine (on le nommera data içi)
    5. Pour avoir le chemin nous allons utiliser os
        ```
        # Dans le cas ou le module est à la racine :
        directory = os.path.dirname(__file__)
        # Dans le cas ou le module est lui même dans un dossier:
        directory = os.path.dirname(os.path.dirname(__file__))
        path_to_file = os.path.join(directory, "data", data_file)
        ```
- On importe nos modules dans le script principal parite.py et on appelle leurs fonctions:
    Tout d'abord l'import :
    ```
    import xml_analysis as x_an
    import csv_analysis as c_an
    ```
    Et l'appel :
    ```
    x_an.launch_analysis('file_name')
    c_an.launch_analysis('file_name')
    ```
    