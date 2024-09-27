def display_automata(tasks, predecessors_number,arcs_number):
    print("* Creation du graphe d'ordonnancement :")
    print(f"{predecessors_number} sommets")
    print(f"{arcs_number} arcs")
    
    for i in range(len(tasks)+1):
        for task in tasks:
            if i in tasks[task]['predecessors']:
                print(f"{i} -> {task} = {i}")
    print()

    
def create_matrix(tasks):

    print("  0", end="")
    for task in tasks:
        print(f" {task}", end="")
    print()
    
    for task in range(len(tasks)+1):
        print(task, "*", end="")
        for task2 in tasks:
            if task in tasks[task2]['predecessors']:
                print(f" {task}", end="")
            else:
                print(" *", end="")
        print()
    print()

