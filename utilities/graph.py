import networkx as nx
import matplotlib.pyplot as plt


def add_nodes_edges(graph, parent_id, node, counter):
    node_id = next(counter)
    label = f"{node.type} ({node.value})"
    graph.add_node(node_id, label=label)

    if parent_id is not None:
        graph.add_edge(parent_id, node_id)

    for child in node.children:
        add_nodes_edges(graph, node_id, child, counter)


def generate_tree_graph(root):
    graph = nx.DiGraph()
    counter = iter(range(1000))
    root_id = next(counter)
    graph.add_node(root_id, label=f"{root.type} ({root.value})")

    for child in root.children:
        add_nodes_edges(graph, root_id, child, counter)

    return graph


def tree_layout(graph, root=0, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
    if pos is None:
        pos = {}
    children = list(graph.successors(root))
    if not isinstance(width, float):
        width = float(width)
    if len(children) != 0:
        dx = width / len(children)
        nextx = xcenter - width / 2 - dx / 2
        for child in children:
            nextx += dx
            pos = tree_layout(graph, root=child, width=dx, vert_gap=vert_gap, vert_loc=vert_loc - vert_gap,
                              xcenter=nextx, pos=pos, parent=root)
    pos[root] = (xcenter, vert_loc)
    return pos


def draw_tree_to_file(tree, file_path):
    graph = generate_tree_graph(tree)
    pos = tree_layout(graph)
    labels = nx.get_node_attributes(graph, 'label')

    plt.figure(figsize=(20, 20))
    nx.draw(graph, pos, labels=labels, with_labels=True, arrows=False, node_size=2000, font_size=10)
    plt.title("Abstract Syntax Tree (AST)")
    plt.savefig(file_path)
    plt.close()


def draw_tree(tree):
    graph = generate_tree_graph(tree)
    pos = tree_layout(graph)
    labels = nx.get_node_attributes(graph, 'label')

    plt.figure(figsize=(25, 25))
    nx.draw(graph, pos, labels=labels, with_labels=True, arrows=False, node_size=2000, font_size=10)
    plt.title("Abstract Syntax Tree (AST)")
    plt.show()
