import sys

grafo = {
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
    'Timisoara': ['Lugoj', 'Arad'],
    'Sibiu': ['Rimnicu-Vilcea', 'Oradea', 'Arad', 'Fagaras'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Rimnicu-Vilcea', 'Drobeta', 'Pitesti'],
    'Pitesti': ['Bucareste', 'Craiova', 'Rimnicu-Vilcea'],
    'Rimnicu-Vilcea': ['Pitesti', 'Sibiu', 'Craiova'],
    'Fagaras': ['Sibiu', 'Bucareste'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Bucareste': ['Pitesti', 'Fagaras'],
    'Zerind': ['Oradea', 'Arad']
}


def dfs(grafo, no, visitado):
    if no not in visitado:
        visitado.append(no)

        if no == 'Bucareste':
            print(visitado)
            sys.exit()

        print(visitado)
        for n in grafo[no]:
            dfs(grafo, n, visitado)


dfs(grafo, 'Arad', [])
