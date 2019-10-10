"""Topological Sort Algorithm"""


def topo_sort(outgoings):
    """Topologcial sort of DAG
    :param outgoings: a dictionary containing outgoings vertices of each vertex
    :return: the topological sort of vertices
    """

    start = {v: 0 for v in outgoings}
    end = {v: 0 for v in outgoings}
    order = 0

    def depth_first_search(v):
        nonlocal start, end, order
        if start[v] != 0:  # already visited
            return

        order += 1
        start[v] = order
        for w in outgoings[v]:
            depth_first_search(w)
        order += 1
        end[v] = order

    for k in outgoings:
        depth_first_search(k)

    def finish_order(v):
        nonlocal end
        return end[v]

    return sorted(outgoings.keys(), key=finish_order, reverse=True)


if __name__ == '__main__':
    outgoings = {
        'shirt': ['tie', 'belt'],
        'tie': ['jacket'],
        'jacket': [],
        'watch': [],
        'under_wears': ['pants', 'shoes'],
        'pants': ['belt', 'shoes'],
        'belt': ['jacket'],
        'socks': ['shoes'],
        'shoes': [],
    }
    topo_order = topo_sort(outgoings)
    print(topo_order)
