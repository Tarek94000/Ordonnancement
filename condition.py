from collections import deque

def verifiying_ord_graph(tasks):
    
    # Vérifier les durées négatives dans les tâches
    for task, info in tasks.items():
        if info['duration'] < 0:
            print(f"-> La tâche {task} a une durée négative. Le graphe n'est donc pas valide pour l'ordonnancement. ", end= "")
            return None, False
    
    # Calculer les degrés entrants en fonction du nombre de prédécesseurs
    in_degree = {task: len(info['predecessors']) for task, info in tasks.items()}

    # File d'attente pour les nœuds sans arêtes entrantes (degré entrant de 0)
    queue = deque([task for task in tasks if in_degree[task] == 0])
    
    topological_order = []
    print("\nIl y a un seul point d’entrée, 0")
    print(f"Il y a un seul point de sortie, {max(tasks.keys())}\n")
    print("* Détection de circuit:\n")
    
    while queue:
        # Imprimer les points d'entrée actuels
        print(f"Points d’entrée : {' '.join(map(str, queue))}")
        
        # Supprimer le premier point d'entrée
        current_task = queue.popleft()
        topological_order.append(current_task)

        print(f"Suppression des points d’entrée : {current_task}")
        
        # Diminuer le degré entrant des successeurs
        for successor, info in tasks.items():
            if current_task in info['predecessors']:
                in_degree[successor] -= 1
                if in_degree[successor] == 0:
                    queue.append(successor)

        # Imprimer les tâches restantes après chaque suppression
        remaining_tasks = [task for task in tasks if task not in topological_order]
        if remaining_tasks:
            print(f"Sommets restant : {' '.join(map(str, remaining_tasks))}\n")
        else:
            print("Sommets restant : Aucun\n")
        
    
    # Vérification finale du circuit
    if len(topological_order) != len(tasks):
        print("-> Le graphe contient un circuit. Il n'est donc pas valide pour l'ordonnancement. ", end= "")
        return None, False  # Indique qu'un cycle a été détecté
    else:
        print("-> Il n’y a pas de circuit.")
        print("-> Il n’y a pas d’arcs négatifs")
        print("-> C’est un graphe d’ordonnancement.\n")
        return topological_order, True  # Aucun cycle détecté


