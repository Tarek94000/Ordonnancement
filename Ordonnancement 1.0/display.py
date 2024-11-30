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

