def calculate_earliest_times(tasks, top_order):
    # Initialiser les temps de début et de fin les plus précoces
    earliest_start = {task: 0 for task in tasks}
    earliest_finish = {task: 0 for task in tasks}
    
    # Passage en avant à travers l'ordre topologique
    for task in top_order:
        earliest_finish[task] = earliest_start[task] + tasks[task]['duration']
        
        # Mettre à jour le temps de début le plus précoce de chaque successeur
        for successor in tasks:
            if task in tasks[successor]['predecessors']:
                earliest_start[successor] = max(earliest_start[successor], earliest_finish[task])
    
    return earliest_start, earliest_finish


def calculate_latest_times(tasks, top_order, earliest_finish):
    # Initialiser les temps de début et de fin les plus tardifs
    latest_finish = {task: float('inf') for task in tasks}
    latest_start = {task: float('inf') for task in tasks}
    
    # Définir le temps de fin le plus tardif du nœud de fin fictif à son temps de fin le plus précoce
    end_task = top_order[-1]
    latest_finish[end_task] = earliest_finish[end_task]
    latest_start[end_task] = latest_finish[end_task] - tasks[end_task]['duration']
    
    # Passage en arrière à travers l'ordre topologique
    for task in reversed(top_order):
        for predecessor in tasks[task]['predecessors']:
            latest_finish[predecessor] = min(latest_finish[predecessor], latest_start[task])
            latest_start[predecessor] = latest_finish[predecessor] - tasks[predecessor]['duration']
    
    return latest_start, latest_finish


def calculate_slack(earliest_start, latest_start):
    # La marge est la différence entre le début le plus tardif et le début le plus précoce
    slack = {task: latest_start[task] - earliest_start[task] for task in earliest_start}
    return slack


def display_slack(slack):
    print("\nMarges (Slacks) pour chaque tâche:")
    for task, sl in slack.items():
        print(f"Tâche {task}: Marge = {sl}")


def find_critical_path(slack):
    # Les tâches avec une marge nulle sont sur le chemin critique
    critical_path = [task for task, sl in slack.items() if sl == 0]
    return critical_path


def display_critical_path(tasks, critical_path):
    print("\nChemin(s) critique(s):")
    # Créer une chaîne de tâches dans l'ordre du chemin critique
    path_sequence = " → ".join(f"Tâche {task}" for task in critical_path)
    print(path_sequence)
