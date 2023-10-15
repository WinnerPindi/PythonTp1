import random
import datetime, time

# Enregistrez l'heure de début de jeu
heureDebut = datetime.datetime.today()

# Deamnde à l'utilisateur d'effectuer un choix 
entree_utilisateur = input('Entrez soit Roche (R) , Papier (P) ou Ciseau (C) : ')
premierlettre = entree_utilisateur[0]

# Convertir l'entrée en minuscules et prendre le premier caractère
entree_utilisateur = entree_utilisateur.lower()
# Liste des choix possibles
choix = ['roche', 'papier', 'ciseau']  # Convertir les choix en minuscules

# Choix aléatoire de la part de l'ordinateur 
choix_ordinateur = random.choice(choix)

# Si l'utilisateur tape exit
if entree_utilisateur == 'exit':
    print("\033[91m Fin de la partie \033[0m")
    exit()

    
# Condition pour La Roche

elif (entree_utilisateur == 'roche' or premierlettre == 'r') and  choix_ordinateur == 'roche':
    print('Voici le choix de l\'ordinateur : ' + choix_ordinateur)
    print('{} et {} c\'est le même choix'.format(entree_utilisateur, choix_ordinateur))

elif (entree_utilisateur == 'roche' or premierlettre == 'r') and  choix_ordinateur == 'papier':
    print('Voici le choix de l\'ordinateur : ' + choix_ordinateur)
    print('L\'ordinateur a gagné, {} perd contre {}'.format(entree_utilisateur, choix_ordinateur))

elif (entree_utilisateur == 'roche' or premierlettre == 'r') and choix_ordinateur == 'ciseau':
    print('Voici le choix de l\'ordinateur : ' + choix_ordinateur)
    print('Félicitations ! Vous avez gagné, {} gagne contre {}'.format(entree_utilisateur, choix_ordinateur))

# Condition pour Le papier

elif (entree_utilisateur == 'papier' or premierlettre == 'p') and choix_ordinateur == 'papier':
    print('Voici le choix de l\'ordinateur : ' + choix_ordinateur)
    print('{} et {} c\'est le même choix'.format(entree_utilisateur, choix_ordinateur))

elif (entree_utilisateur == 'papier' or premierlettre == 'p') and choix_ordinateur == 'roche':
    print('Voici le choix de l\'ordinateur : ' + choix_ordinateur)
    print('Félicitations ! Vous avez gagné, {} gagne contre {}'.format(entree_utilisateur, choix_ordinateur))

elif (entree_utilisateur == 'papier' or premierlettre == 'p') and  choix_ordinateur == 'ciseau':
    print('Voici le choix de l\'ordinateur : ' + choix_ordinateur)
    print('L\'ordinateur a gagné, {} perd contre {}'.format(entree_utilisateur, choix_ordinateur))


# Condition pour Le ciseau

elif (entree_utilisateur == 'ciseau' or premierlettre == 'r') and choix_ordinateur == 'ciseau':
    print('Voici le choix de l\'ordinateur : ' + choix_ordinateur)
    print('{} et {} c\'est le même choix'.format(entree_utilisateur, choix_ordinateur))

elif (entree_utilisateur == 'ciseau' or premierlettre == 'r') and choix_ordinateur == 'roche':
    print('Voici le choix de l\'ordinateur : ' + choix_ordinateur)
    print('L\'ordinateur a gagné, {} perd contre {}'.format(entree_utilisateur, choix_ordinateur))

elif (entree_utilisateur == 'ciseau' or premierlettre == 'r') and choix_ordinateur == 'papier':
    print('Voici le choix de l\'ordinateur : ' + choix_ordinateur)
    print('Félicitations ! Vous avez gagné, {} gagne contre {}'.format(entree_utilisateur, choix_ordinateur))


# Condition au cas où l'utilisateur entre d'autres informations 
else:
    print("\033[91mVeuillez choisir parmis les options demandées. Vous devez relancer le programme \033[0m")
    exit()


# Enregstrer l'heure de la fin
heureFin = datetime.datetime.today()

# Calcul du temps écoulé pendant le jeu 

tempsEcoule = heureFin - heureDebut

# Afficher le temps de début, de fin et le temps écoulé 
print("Heure de début du jeu:", heureDebut)
print("Heure de fin du jeu:", heureFin)
print("Temps écoulé pendant le jeu:", tempsEcoule, "secondes")

# Calcul de la moyenne du temps joué 
moyenne_temps_joue = tempsEcoule/2
print("Moyenne du temps joué pour l'ordinateur et l'utilisateur:", moyenne_temps_joue, "secondes")
