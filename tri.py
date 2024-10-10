import os
import shutil  # Pour déplacer/copier les fichiers
import subprocess

def test_open_door(log_file):
    """
    Fonction pour tester un fichier log avec canplayer et vérifier si les portes s'ouvrent.
    """
    print(f"Test de {log_file}...")

    # Exécuter la commande canplayer
    try:
        subprocess.run(['canplayer', '-I', log_file], check=True)
    except subprocess.CalledProcessError:
        print(f"Erreur lors de l'exécution de canplayer avec {log_file}")
        return False

    # Demander à l'utilisateur si les portes se sont ouvertes
    opened = input("Les portes se sont-elles ouvertes ? (y/n): ").strip().lower()

    if opened == 'y':
        print(f"Les portes se sont ouvertes avec {log_file}.")

        # Ajouter un message pour refermer les portes avant de continuer
        input("Veuillez refermer les portes manuellement, puis appuyez sur Entrée pour continuer...")
        return True
    else:
        return False

def split_file(log_file, part1, part2):
    """
    Diviser le fichier log en deux parties : part1 et part2.
    """
    with open(log_file, 'r') as f:
        lines = f.readlines()

    middle = len(lines) // 2

    with open(part1, 'w') as f1:
        f1.writelines(lines[:middle])

    with open(part2, 'w') as f2:
        f2.writelines(lines[middle:])

def find_opening_log(log_file, destination_dir):
    """
    Fonction récursive qui divise le fichier en deux et teste chaque partie pour trouver celle qui ouvre les portes.
    """
    # Si le fichier ne contient que peu de lignes, il est trop petit pour être divisé
    with open(log_file, 'r') as f:
        lines = f.readlines()

    if len(lines) <= 1:
        print(f"Fichier trop petit pour être divisé : {log_file}")
        return

    # Diviser le fichier en deux parties
    part1 = 'part1.log'
    part2 = 'part2.log'
    split_file(log_file, part1, part2)

    # Tester la première partie
    if test_open_door(part1):
        final_file = 'porte.log'
        os.rename(part1, final_file)
        os.remove(part2)
        print("Le fichier a été renommé en porte.log.")
        find_opening_log(final_file, destination_dir)
        move_to_destination(final_file, destination_dir)
    # Tester la deuxième partie
    elif test_open_door(part2):
        final_file = 'porte.log'
        os.rename(part2, final_file)
        os.remove(part1)
        print("Le fichier a été renommé en porte.log.")
        find_opening_log(final_file, destination_dir)
        move_to_destination(final_file, destination_dir)
    else:
        print("Aucune des parties ne semble ouvrir les portes.")
        os.remove(part1)
        os.remove(part2)

def move_to_destination(file_name, destination_dir):
    """
    Fonction pour déplacer le fichier final vers un répertoire spécifique.
    """
    try:
        # Créer le dossier de destination s'il n'existe pas
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Construire le chemin complet vers le fichier de destination
        destination_path = os.path.join(destination_dir, file_name)

        # Déplacer le fichier vers l'emplacement désiré
        shutil.move(file_name, destination_path)
        print(f"Fichier {file_name} déplacé avec succès vers {destination_path}")
    except
