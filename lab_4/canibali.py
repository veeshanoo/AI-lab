from copy import deepcopy as dp
from pprint import pprint as pp

N = 5
M = 3

class Node:
    def __init__(self, config):
        self.config = config

    def expand(self):
        node_cpy = dp(self.config)
        config_lst = []

        mal_current = node_cpy[0]
        misi = node_cpy[1 + mal_current][0]
        cani = node_cpy[1 + mal_current][1]

        misi_calatori = min(M, misi)

        for misi_barca in range(misi_calatori + 1):
            if misi_barca == 0:
                cani_calatori = min(cani, M)
            else:
                cani_calatori = min(cani, M - misi_barca, misi_barca)

            for cani_barca in range(cani_calatori + 1):
                new_mal = 1 - mal_current
                new_misi = misi - misi_barca
                new_cani = cani - cani_barca
                new_misi_opus = N - new_misi
                new_cani_opus = N - new_cani

                if new_cani > new_misi > 0:
                    continue

                if new_cani_opus > new_misi_opus > 0:
                    continue

                if misi_barca + cani_barca == 0:
                    continue

                new_state = [new_mal, [], []]
                new_state[1 + new_mal] = [new_misi_opus, new_cani_opus]
                new_state[2 - new_mal] = [new_misi, new_cani]

                config_lst.append(Node(new_state))

        return config_lst

    def __eq__(self, other):
        return self.config == other.config

    def __repr__(self):
        return str(self.config)


class PathNode:
    def __init__(self, node, cost, parent_node):
        self.parent_node = parent_node
        self.node = node
        self.cost = cost

    def heuristic(self):
        tg = target_node.config
        cnt = 0

        mal = tg[0]
        misi = tg[1][0]
        cani = tg[1][1]

        cnt = (misi + cani) // M
        if (misi + cani) % M > 0:
            cnt += 1

        if mal == 0:
            cnt -= 1

        return cnt

    def __repr__(self):
        return str(self.node.config) + ", " + str(self.cost)


visited = []

if __name__ == '__main__':
    start_node = Node([0, [N, N], [0, 0]])
    target_node = Node([1, [0, 0], [N, N]])

    open_list = [PathNode(dp(start_node), 0, None)]
    visited = [PathNode(dp(start_node), 0, None)]

    while len(open_list) > 0:
        open_list.sort(key=lambda pth: pth.cost + pth.heuristic())
        current = open_list.pop(0)
        if current.node == target_node:
            print("Nr of moves: " + str(current.cost))
            it = current
            while True:
                print(it.node)
                if it.parent_node is None:
                    break
                it = it.parent_node
            break

        for nxt in current.node.expand():
            # pp(nxt)
            new_cost = current.cost + 1
            old_path_node = next((node for node in visited if node.node == nxt), None)

            if old_path_node is None:
                open_list.append(PathNode(nxt, new_cost, current))
                visited.append(PathNode(nxt, new_cost, current))
            else:
                if new_cost < old_path_node.cost:
                    open_list = [x for x in open_list if x.node != old_path_node.node]
                    visited = [x for x in visited if x.node != old_path_node.node]
                    open_list.append(PathNode(nxt, new_cost, current))
                    visited.append(PathNode(nxt, new_cost, current))