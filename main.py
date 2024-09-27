from display import *
from process import *

def read_automata(file_name):
    tasks = {}
    predecessors_number = 0
    arcs_number = 0

    with open(file_name, 'r') as file:
        lines = file.read().splitlines()

        for line in lines:
            parts = line.split()
            task_num = int(parts[0])
            duration = int(parts[1])
            
            if len(parts) > 2:
                predecessors = list(map(int, parts[2:]))
                predecessors_number += len(predecessors)
                arcs_number += len(predecessors)
            else:
                predecessors = [0]
                arcs_number += len(predecessors)
                
            tasks[task_num] = {
                'duration': duration,
                'predecessors': predecessors
            }

    return tasks, predecessors_number, arcs_number


tasks, predecessors_number, arcs_number = read_automata("Diaries/Diary2.txt")

display_automata(tasks, predecessors_number, arcs_number)
create_matrix(tasks)
