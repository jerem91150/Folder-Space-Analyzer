import os
import easygui

def get_size(start_path):
    """Calcule la taille totale d'un dossier ou fichier."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Ajoute la taille du fichier au total
            total_size += os.path.getsize(fp)
    return total_size

def analyser_dossier(dossier_path):
    print(f"Analyse de l'utilisation de l'espace dans {dossier_path}:")
    sous_dossiers = []
    
    # Récupère tous les sous-dossiers dans le dossier spécifié
    for item in os.listdir(dossier_path):
        itempath = os.path.join(dossier_path, item)
        if os.path.isdir(itempath):
            sous_dossiers.append((item, get_size(itempath)))

    # Trie les sous-dossiers par taille décroissante
    sous_dossiers.sort(key=lambda x: x[1], reverse=True)

    # Affiche les résultats dans la console
    print(f"{'Sous-dossier':<30} Taille (Go)")
    print("-" * 40)
    for sous_dossier, size in sous_dossiers:
        print(f"{sous_dossier:<30} {size / (1024 ** 3):.2f} Go")

def select_folder():
    folder_selected = easygui.diropenbox(title="Sélectionnez un dossier à analyser")
    if folder_selected:
        analyser_dossier(folder_selected)
    else:
        print("Aucun dossier sélectionné.")

if __name__ == "__main__":
    select_folder()
    # Pause à la fin pour que l'utilisateur puisse voir les résultats
    input("\nAppuyez sur Entrée pour fermer le programme...")
