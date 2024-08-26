import os
import easygui
import csv
from concurrent.futures import ThreadPoolExecutor

def format_size(size_bytes):
    """Formate la taille en unités lisibles."""
    for unit in ['', 'Ko', 'Mo', 'Go', 'To']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0

def get_size(start_path):
    """Calcule la taille totale d'un dossier ou fichier."""
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
    except PermissionError:
        print(f"Erreur de permission lors de l'accès à {start_path}")
    return total_size

def analyser_dossier(dossier_path, profondeur=1):
    print(f"Analyse de l'utilisation de l'espace dans {dossier_path}:")
    sous_dossiers = []
    
    with ThreadPoolExecutor() as executor:
        futures = []
        for item in os.listdir(dossier_path):
            itempath = os.path.join(dossier_path, item)
            if os.path.isdir(itempath):
                futures.append(executor.submit(get_size, itempath))
        
        for item, future in zip(os.listdir(dossier_path), futures):
            if os.path.isdir(os.path.join(dossier_path, item)):
                sous_dossiers.append((item, future.result()))

    sous_dossiers.sort(key=lambda x: x[1], reverse=True)

    print(f"{'Sous-dossier':<30} Taille")
    print("-" * 40)
    for sous_dossier, size in sous_dossiers:
        print(f"{sous_dossier:<30} {format_size(size)}")
    
    return sous_dossiers

def exporter_resultats(resultats, chemin_fichier):
    with open(chemin_fichier, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Sous-dossier', 'Taille (octets)', 'Taille formatée'])
        for sous_dossier, size in resultats:
            writer.writerow([sous_dossier, size, format_size(size)])

def menu_principal():
    choices = ["Analyser un dossier", "Quitter"]
    choice = easygui.buttonbox("Que voulez-vous faire ?", "Menu principal", choices=choices)
    
    if choice == "Analyser un dossier":
        folder_selected = easygui.diropenbox(title="Sélectionnez un dossier à analyser")
        if folder_selected:
            resultats = analyser_dossier(folder_selected)
            if easygui.ynbox("Voulez-vous exporter les résultats?", "Exporter"):
                fichier_export = easygui.filesavebox(default="resultats.csv", filetypes=["*.csv"])
                if fichier_export:
                    exporter_resultats(resultats, fichier_export)
                    print(f"Résultats exportés dans {fichier_export}")
        else:
            print("Aucun dossier sélectionné.")
    elif choice == "Quitter":
        return False
    
    return True

if __name__ == "__main__":
    while menu_principal():
        pass
    print("Programme terminé.")