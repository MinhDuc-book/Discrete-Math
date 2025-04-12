class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

# Khởi tạo đồ thị dưới dạng danh sách cạnh
edges = [
    Edge("Deep Springs", "Oasis", 10),
    Edge("Lida", "Gold Point", 12),
    Edge("Silver Pea", "Goldfield", 20),
    Edge("Lida", "Goldfield", 20),
    Edge("Dyer", "Oasis", 21),
    Edge("Oasis", "Silver Pea", 23),
    Edge("Dyer", "Silver Pea", 25),
    Edge("Oasis", "Lida", 25),
    Edge("Tonopah", "Manhattan", 25),
    Edge("Deep Springs", "Gold Point", 30),
    Edge("Goldfield", "Tonopah", 35),
    Edge("Silver Pea", "Tonopah", 40),
    Edge("Gold Point", "Beatty", 45),
    Edge("Tonopah", "Warm Springs", 55),
    Edge("Warm Springs", "Manhattan", 60),
    Edge("Beatty", "Goldfield", 70),
    Edge("Dyer", "Manhattan", 80)
]

# Kiểm tra trọng số âm
for edge in edges:
    if edge.weight < 0:
        raise ValueError(f"Trọng số âm không hợp lệ: {edge.u} - {edge.v}")

# Sắp xếp các cạnh theo trọng số
edges.sort(key=lambda edge: edge.weight)

# Khởi tạo tập hợp (Union-Find)
parent = {}
rank = {}

def find(node):
    """Tìm gốc của tập hợp chứa node, sử dụng path compression."""
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node1, node2):
    """Hợp nhất hai tập hợp, sử dụng union by rank."""
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

# Khởi tạo các nút trong đồ thị
for edge in edges:
    if edge.u not in parent:
        parent[edge.u] = edge.u
        rank[edge.u] = 0
    if edge.v not in parent:
        parent[edge.v] = edge.v
        rank[edge.v] = 0

# Thuật toán Kruskal
mst = []
for edge in edges:
    if find(edge.u) != find(edge.v):
        mst.append(edge)
        union(edge.u, edge.v)

# Kiểm tra đồ thị liên thông
def is_connected():
    roots = set(find(node) for node in parent)
    return len(roots) == 1

# Kết quả
print("Danh sách các cạnh trong cây khung nhỏ nhất:")
for edge in mst:
    print(f"Cạnh: {edge.u} - {edge.v}, Trọng số: {edge.weight}")

print(f"Tổng số cạnh trong cây khung: {len(mst)}")
total_weight = sum(edge.weight for edge in mst)
print(f"Tổng trọng số của cây khung: {total_weight}")

if is_connected():
    print("Đồ thị liên thông, MST hợp lệ.")
else:
    print("Cảnh báo: Đồ thị không liên thông, kết quả là rừng khung.")