## Auxiliary Functions ##
## This functions are used to display the configuration of the Hanoi towers. ##

def display(tower_list):
    n = max([len(t) for t in tower_list])
    for idx in range(n-1, -1, -1):
        line_txt = "\t"
        for t in tower_list:
            if len(t) > idx:
                line_txt += str(t[idx]) + "\t"
            else:
                line_txt +=" \t"
        print(line_txt)
    print("-"*len(tower_list)*5)


def move(source, target, tower_list):
    top_disk = tower_list[source].pop()
    tower_list[target].append(top_disk)
    return tower_list

###############################################

def tower(n, source, target, aux, tower_list):
    if n == 1:
        tower_list = move(source, target, tower_list)
        display(tower_list)
        return
    else:
        tower(n-1, source, aux, target, tower_list)
        tower_list = move(source, target, tower_list)
        display(tower_list)
        tower(n-1, aux, target, source, tower_list)
        return

if __name__=="__main__":

    n = 4
    A = ["A"] + [k for k in range(n, 0, -1)]
    B = ["B", ]
    C = ["C", ]

    tower_list = [A, B, C]

    tower(n, 0, 2, 1, tower_list)
