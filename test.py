from read_display import *
from process import *
from condition import *
import sys

def main():
    print("\n----- ORDONNANCEMENT -----")
    for i in range(1, 15):  # Boucle pour les fichiers de 1 à 14
        tasks = {}
        arcs_number = 0
        top_order = []
        earliest_finish = {}
        latest_start = {}
        latest_finish = {}
        slack = {}
        critical_path = []     

        file_name = f"Tables/table {i}.txt"
        output_file = f"Tests/test {i}.txt"

        # Rediriger les sorties vers un fichier
        with open(output_file, "w") as f:
            sys.stdout = f  # Rediriger print vers le fichier
            try:
                # Étape 1 : Lire le tableau des contraintes à partir du fichier
                tasks, arcs_number = read_automata(file_name)

                # Étape 2 : Créer et afficher la matrice du graphe
                display_automata(tasks, arcs_number)
                print("\n* Représentation du Graphe (Matrice) :\n")
                create_matrix(tasks)

                # Étape 3 : Vérifier si le graphe est un graphe d'ordonnancement valide
                top_order, is_acyclic = verifiying_ord_graph(tasks)

                if not is_acyclic:
                    print("Veuillez choisir un autre tableau.")
                    continue

                print("\nGraphe d'ordonnancement valide. Poursuite des calculs...\n")

                # Étape 4 : Calculer les temps au plus tôt et au plus tard
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

            except Exception as e:
                # En cas d'erreur
                print(f"Erreur lors du traitement du fichier {file_name}: {e}")

        # Restaurer la sortie standard
        sys.stdout = sys.__stdout__
        print(f"Résultats enregistrés dans {output_file}")

if __name__ == "__main__":
    main()



###################################### Test functions ########################################
"""tasks, arcs_number = read_automata(f"Tables/table 6.txt")

display_automata(tasks, arcs_number)

print("\nReprésentation du Graphe (Matrice) :\n")
create_matrix(tasks)"""

# Fonction de test
"""
tasks, arcs_number = read_automata(f"Tables/table 5.txt")

display_automata(tasks, arcs_number)

print("\nReprésentation du Graphe (Matrice) :\n")
create_matrix(tasks)

top_order, is_acyclic = verifiying_ord_graph(tasks)

if not is_acyclic:
    print("le graphe n'est donc pas valide pour l'ordonnancement. Veuillez choisir un autre tableau.")
    exit()

earliest_start, earliest_finish = calculate_earliest_times(tasks, top_order)
latest_start, latest_finish = calculate_latest_times(tasks, top_order, earliest_finish)

print("\nTemps au plus tôt (EST) et au plus tard (EFT) :")
for task in tasks:
    print(f"Tâche {task} : EST = {earliest_start[task]}, EFT = {earliest_finish[task]}")
    
print("\nTemps au plus tard (LST) et au plus tard (LFT) :")
for task in tasks:
    print(f"Tâche {task} : LST = {latest_start[task]}, LFT = {latest_finish[task]}")
    
slack = calculate_slack(earliest_start, latest_start)
print("\nMarges (Slack) :")
for task in tasks:
    print(f"Tâche {task} : Marge = {slack[task]}")
"""