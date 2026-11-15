# Application de gestion des taches (console)
# Projet Git / GitHub - Licence 1

taches = []


def afficher_menu():
    print("\n=== GESTION DES TACHES ===")
    print("1. Ajouter une tache")
    print("2. Afficher les taches")
    print("3. Rechercher une tache")
    print("0. Quitter")


def ajouter_tache():
    titre = input("Titre de la tache : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas etre vide.")
    else:
        taches.append(titre)
        print("Tache ajoutee avec succes.")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tache pour le moment.")
    else:
        print("\nListe des taches :")
        for i in range(len(taches)):
            print(f"{i + 1}. {taches[i]}")


def rechercher_tache():
    mot = input("Mot-cle a rechercher : ").strip().lower()
    trouve = False
    for i in range(len(taches)):
        if mot in taches[i].lower():
            print(f"{i + 1}. {taches[i]}")
            trouve = True
    if not trouve:
        print("Aucune tache trouvee.")


choix = ""
while choix != "0":
    afficher_menu()
    choix = input("Votre choix : ").strip()

    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        rechercher_tache()
    elif choix == "0":
        print("Au revoir !")
    else:
        print("Choix invalide, veuillez reessayer.")
