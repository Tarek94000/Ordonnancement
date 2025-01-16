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
    
    return latest_start


def calculate_slack(earliest_start, latest_start):
    # La marge est la différence entre le début le plus tardif et le début le plus précoce
    slack = {task: latest_start[task] - earliest_start[task] for task in earliest_start}
    return slack


def calculate_task_ranks(tasks):
    ranks = {}
    
    # Fonction récursive pour calculer le rang
    def compute_rank(task_id):
        if task_id in ranks:
            return ranks[task_id]  # Déjà calculé
        if not tasks[task_id]['predecessors']:
            ranks[task_id] = 0  # Pas de prédécesseur -> rang 0
        else:
            ranks[task_id] = 1 + max(compute_rank(pred) for pred in tasks[task_id]['predecessors'])
        return ranks[task_id]
    
    # Calculer les rangs pour toutes les tâches
    for task_id in tasks:
        compute_rank(task_id)
    
    return ranks

def find_all_paths(tasks, slack, start_task, end_task):
    def dfs(current_task, path):
        # Add current task to the path
        path.append(current_task)

        # If the end task is reached, save the path
        if current_task == end_task:
            critical_paths.append(list(path))
        else:
            # Explore successors with zero slack
            for successor in tasks:
                if current_task in tasks[successor]['predecessors'] and slack[successor] == 0:
                    dfs(successor, path)

        # Backtrack
        path.pop()

    # List to store all critical paths
    critical_paths = []

    # Start DFS from the starting task
    dfs(start_task, [])

    return critical_paths

def find_critical_path(tasks, paths):
    path_durations_table = []
    for path in paths:
        path_durations = 0
        for task in path:
            path_durations += tasks[task]['duration']
        path_durations_table.append(path_durations)

    critical_paths = []       
    for i,path in enumerate(path_durations_table):
        if path == max(path_durations_table):
            critical_paths.append(paths[i])

    return critical_paths
    

            
