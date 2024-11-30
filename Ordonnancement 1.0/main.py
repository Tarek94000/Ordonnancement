from display import *
from scheduling import *
from condition import *

# Fonction pour lire le tableau des contraintes à partir d'un fichier
def read_automata(file_name):
    tasks = {0: {'duration': 0, 'predecessors': []}}  # Add node 0 with no predecessors and no duration
    arcs_number = 0

    with open(file_name, 'r') as file:
        lines = file.read().splitlines()

        for line in lines:
            parts = line.split()
            task_num = int(parts[0])
            duration = int(parts[1])
            
            if len(parts) > 2:
                predecessors = list(map(int, parts[2:]))
                arcs_number += len(predecessors)
            else:
                predecessors = [0]  # Connect to fictitious start node
                arcs_number += 1
                
            tasks[task_num] = {
                'duration': duration,
                'predecessors': predecessors
            }

    # Find tasks with no successors
    all_tasks = set(tasks.keys())
    tasks_with_successors = set()
    
    for task_info in tasks.values():
        tasks_with_successors.update(task_info['predecessors'])

    terminal_tasks = all_tasks - tasks_with_successors  # These are the tasks with no successors

    # Add a fictitious end node (end_node = N + 1 where N is the number of real tasks)
    end_node = len(tasks)
    tasks[end_node] = {'duration': 0, 'predecessors': list(terminal_tasks)}  # End node

    arcs_number += len(terminal_tasks)

    return tasks, arcs_number


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


##############################################      MAIN      ################################################################
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

##################################################################################################################################

"""tasks, arcs_number = read_automata(f"Tables/table 6.txt")

display_automata(tasks, arcs_number)

print("\nReprésentation du Graphe (Matrice) :\n")
create_matrix(tasks)"""