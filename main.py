from read_display import *
from process import *
from condition import *

def main():
    print("\n----- ORDONNANCEMENT -----")
    while True:
        
        # Initialisation des variables par sécurité
        tasks = {}
        arcs_number = 0
        top_order = []
        earliest_finish = {}
        earliest_finish = {}
        latest_start = {}
        latest_finish = {}
        slack = {}
        critical_path = []     
        
        user_input = input("Entrez le numero du fichier de contraintes (entre 1 et 14) : ")
        
        try:
            # Essayer de convertir l'entrée en un entier
            number = int(user_input)
            
            # Regarde si le nombre est dans la plage autorisée
            if number < 1 or number > 14:
                print("\nVeuillez entrer un nombre valide.")  # Hors de la plage autorisée
                continue
        
        except ValueError:
            # Si l'entrée n'est pas un nombre
            print("\nEntrée invalide. Veuillez entrer un nombre valide.")
            continue
        
        file_name = f"Tables/table {number}.txt"

        # Étape 1 : Lire le tableau des contraintes à partir du fichier
        tasks, arcs_number = read_automata(file_name)

        # Étape 2 : Créer et afficher la matrice du graphe
        display_automata(tasks, arcs_number)
        print("\nReprésentation du Graphe (Matrice) :\n")
        create_matrix(tasks)

        # Étape 3 : Vérifier si le graphe est un graphe d'ordonnancement valide (en utilisant verifiying_ord_graph)
        top_order, is_acyclic = verifiying_ord_graph(tasks)

        if not is_acyclic:
            print("Veuillez choisir un autre tableau.")
            continue

        print("\nGraphe d'ordonnancement valide. Poursuite des calculs...\n")

        # Étape 4 : Calculer les temps au plus tôt et au plus tard (passage avant et arrière)
        earliest_start, earliest_finish = calculate_earliest_times(tasks, top_order)
        latest_start, latest_finish = calculate_latest_times(tasks, top_order, earliest_finish)

        # Afficher les résultats
        print("\nTemps au plus tôt (EST) et au plus tard (EFT) :")
        for task in tasks:
            print(f"Tâche {task} : EST = {earliest_start[task]}, EFT = {earliest_finish[task]}")
        
        print("\nTemps au plus tard (LST) et au plus tard (LFT) :")
        for task in tasks:
            print(f"Tâche {task} : LST = {latest_start[task]}, LFT = {latest_finish[task]}")

        # Étape 5 : Calculer et afficher les marges (slack)
        slack = calculate_slack(earliest_start, latest_start)
        print("\nMarges (Slack) :")
        for task in tasks:
            print(f"Tâche {task} : Marge = {slack[task]}")

        # Étape 6 : Calculer et afficher le(s) chemin(s) critique(s)
        critical_path = find_critical_path(slack)
        display_critical_path(tasks, critical_path)

        print("\n----- Fin de l'ordonnancement pour ce tableau -----\n")

if __name__ == "__main__":
    main()
