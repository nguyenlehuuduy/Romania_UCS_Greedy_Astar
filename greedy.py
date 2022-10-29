def hcost(path):
    last_node = path[-1]
    h_cost = H_table[last_node]
    return h_cost, last_node


def greedy_search(graph, start_node, stop_node):
    visited = []
    queue = [[(start_node)]]
    while queue:
        queue.sort(key=hcost)
        # pop  loại bỏ phần tử tại vị trí được chỉ định.
        path = queue.pop(0)
        node = path[-1]
        if node in visited:
            continue
        else:
            # append thêm phần tử vào cuối danh sách
            visited.append(node)
            if node == stop_node:
                return path
            else:
                # node liền kề
                adjacent_nodes = graph.get(node)
                for node2 in adjacent_nodes:
                    if node2 in visited:
                        continue
                    new_path = path.copy()
                    new_path.append(node2)
                    queue.append(new_path)


graph = {
    # 'S': ['A', 'B'],
    # 'A': ['S','X','Y'],
    # 'B': ['S','C','D'],
    # 'Y': ['A', 'E'],
    # 'X': ['A','E'],
    # 'C': ['B','E'],
    # 'D': ['B', 'E']
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu',  'Pitesti'],
    'Rimnicu': ['Sibiu', 'Craiova',  'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu', 'Craiova',  'Bucharest'],
    'Bucharest': ['Fagaras',  'Pitesti',  'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui',  'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi'],
}

H_table = {
    # 'S': 20,
    # 'A': 5,
    # 'B': 6,
    # 'C': 4,
    # 'D': 15,
    # 'X': 5,
    # 'Y': 20,
    # 'E': 0,
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu': 193,
    'Fagaras': 176,
    'Pitesti': 100,
    'Bucharest': 0,
    'Giurgiu': 77,
    'Urziceni': 80,
    'Hirsova': 151,
    'Eforie': 161,
    'Vaslui': 199,
    'Iasi': 226,
    'Neamt': 234
}
solution = greedy_search(graph, 'Arad', 'Bucharest')
print('Greedy search from S to E : ', solution)
