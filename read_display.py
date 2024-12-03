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


def display_automata(tasks, arcs_number):
    # Affiche les informations de base sur le graphe d'ordonnancement
    print("* Creation du graphe d'ordonnancement :")
    print(f"{len(tasks)} sommets")  # Affiche le nombre de sommets (tâches)
    print(f"{arcs_number} arcs")    # Affiche le nombre d'arcs

    # Parcourt chaque tâche et ses prédécesseurs pour afficher les arcs
    for i in range(len(tasks)+1):
        for task in tasks:
            if i in tasks[task]['predecessors']:
                print(f"{i} -> {task} = {tasks[i]['duration']}")
    print()


def create_matrix(tasks):
    # Affiche l'en-tête de la matrice
    print("    0", end="")
    for task in tasks:
        if task < 10:
            print(" ", end="")
        print(f"  {task}", end="")
    print()
    
    # Parcourt chaque tâche pour créer les lignes de la matrice
    for task in range(len(tasks)):
        # Si la tâche fait plus de 9, on ajuste l'espacement pour l'affichage
        if task > 9:
            print(task, " *", end="")
        else:
            print(task, "  *", end="")
        
        # Vérifie si la tâche actuelle est un prédécesseur de task2
        for task2 in tasks:
            # Si la tâche fait plus de 9, on ajuste l'espacement pour l'affichage
            if task > 9:
                if task in tasks[task2]['predecessors']:
                    if tasks[task]['duration'] < 10:
                        print(f"   {tasks[task]['duration']}", end="")
                    else:
                        print(f"  {tasks[task]['duration']}", end="")
                else:
                    print("   *", end="")
            
            else:
                if task in tasks[task2]['predecessors']:
                    if tasks[task]['duration'] < 10:
                        print(f"   {tasks[task]['duration']}", end="")
                    else:
                        print(f"  {tasks[task]['duration']}", end="")
                else:
                    print("   *", end="")
        print()
    print()

