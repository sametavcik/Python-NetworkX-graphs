import networkx as nx
import matplotlib.pyplot as plt


def cizdir(g1):

    node_pos = nx.get_node_attributes(g1, 'pos')
    nx.draw_networkx(g1, node_pos,with_labels=True)
    nx.draw_networkx_edges(g1, node_pos, edge_color='black')
    edge_labels = dict([((u, v,), d['weight']) for u, v, d in g1.edges(data=True)])
    nx.draw_networkx_edge_labels(g1, node_pos, edge_labels=edge_labels, label_pos=0.4, font_size=9)

    plt.axis('off')
    plt.show()

def uzunlukbul(g1,source,target):
    try:
        way1 = nx.dijkstra_path(g1, source=source, target=target)
        totalway1 = 0
        for i in range(len(way1) - 1):
            info = g1.get_edge_data(way1[i], way1[i + 1])
            totalway1 += info['weight']
        print("{0} numaralı düğümden {1} numaralı düğüme en kısa uzunluk = ".format(source,target), totalway1)
    except:
            print("{0} numaralı düğümden {1} numaralı düğüme herhangi bir yol bulunamadı ".format(source,target))


def main():
    nodess = [0, 1, 2, 3, 4]
    edges = [(0, 1, 5.0), (0, 2, 3.0), (0, 4, 2.0), (2, 1, 1.0,), (2, 3, 2.0), (4, 1, 6.0), (4, 2, 10.0), (4, 3, 4.0),
             (1, 2, 2.0),(1, 3, 6.0)]

    g1 = nx.DiGraph()
    g1.add_nodes_from(nodess)
    g1.add_weighted_edges_from(edges)

    print(nx.get_edge_attributes(g1,'pos'))

    g1.nodes[0]['pos'] = (3, 2)
    g1.nodes[1]['pos'] = (5, 0)
    g1.nodes[2]['pos'] = (4, -2)
    g1.nodes[3]['pos'] = (2, -2)
    g1.nodes[4]['pos'] = (0.04, -0.1)


    cizdir(g1)

    uzunlukbul(g1,4, 0)
    uzunlukbul(g1,4, 1)
    uzunlukbul(g1,4, 2)
    uzunlukbul(g1,4, 3)

    g1.remove_node(1)

    cizdir(g1)

main()