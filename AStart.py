from collections import deque

# (Khởi tạo lớp)


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        H = {
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

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # (open_list là danh sách các nút đã được truy cập, node nào là neighbors)
        # (bắt đầu với nút bắt đầu)
        # (closed_list là danh sách các nút đã được truy cập)
        # (node neighbors nào được kiểm tra)

        open_list = set([start_node])
        closed_list = set([])

        # (g chứa khoảng cách hiện tại từ start_node đến tất cả các nút khác)
        # (giá trị mặc định (nếu không tìm thấy nó trong bản đồ) là + infinity)
        g = {}

        g[start_node] = 0

        # (parents chứa một bản đồ kề của tất cả các nút)
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # (tìm một nút có giá trị thấp nhất của f () - hàm đánh giá)
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # (nếu nút hiện tại là stop_node)
            # (sau đó bắt đầu tạo lại đường dẫn từ nó đến start_node)
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # (đối với tất cả các node neighbors của nút hiện tại)
            for (m, weight) in self.get_neighbors(n):
                # (nếu nút hiện tại không có trong cả open_list và closed_list)
                # (thêm nó vào open_list và ghi chú n là parent)
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # (nếu không, hãy kiểm tra xem lần đầu tiên truy cập n có nhanh hơn không, sau đó m)
                # (nếu có, hãy cập nhật dữ liệu mẹ và dữ liệu g)
                # (và nếu nút nằm closed_list, di chuyển nút đó sang open_list)
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # (xóa n khỏi open_list và thêm nó vào closed_list)
            #  (bởi vì tất cả các node neighbors đều bị kiểm tra)
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


adjacency_list = {
    # 'S': [('A', 1), ('B', 2)],
    # 'A': [('X', 4), ('Y', 7)],
    # 'B': [('D', 1), ('C', 7)],
    # 'X': [('E', 2)],
    # 'Y': [('E', 3)],
    # 'C': [('E', 5)],
    # 'D': [('E', 12)],
    'Arad': [('Sibiu', 140), ('Zerind', 75), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu', 146), ('Pitesti', 138)],
    'Rimnicu': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)],
}

graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('Arad', 'Bucharest')
