import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
from matplotlib.cm import ScalarMappable
from matplotlib import cm
import numpy as np


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#000000"  # Початковий колір вузла (чорний)
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_tree():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root


def color_gradient(num_nodes):
    cmap = cm.get_cmap('Blues', num_nodes)
    return [to_hex(cmap(i / (num_nodes - 1))) for i in range(num_nodes)]


def bfs(tree_root):
    queue = [tree_root]
    visited = []
    while queue:
        node = queue.pop(0)
        visited.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited


def dfs(tree_root):
    stack = [tree_root]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited


def visualize_traversal(tree_root, traversal_type="bfs"):
    if traversal_type == "bfs":
        order = bfs(tree_root)
    else:
        order = dfs(tree_root)
    
    colors = color_gradient(len(order))
    
    for i, node in enumerate(order):
        node.color = colors[i]
        draw_tree(tree_root)


# Створення дерева
tree_root = build_tree()

# Візуалізація обходу в ширину
visualize_traversal(tree_root, traversal_type="bfs")

# Візуалізація обходу в глибину
visualize_traversal(tree_root, traversal_type="dfs")
