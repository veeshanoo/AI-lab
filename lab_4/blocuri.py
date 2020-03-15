from copy import deepcopy as dp
from pprint import pprint as pp


class Node:
    def __init__(self, config):
        self.config = config

    def expand(self):
        node_cpy = dp(self.config)
        config_lst = []

        for i, lst in enumerate(node_cpy):
            if len(lst) == 0:
                continue

            new_config = dp(node_cpy)

            el = new_config[i].pop(0)

            for j, x in enumerate(new_config):
                if i == j:
                    continue

                nxt_config = dp(new_config)
                nxt_config[j].insert(0, el)

                config_lst.append(Node(nxt_config))

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

    def heuristic(self, target_node):
        tg = target_node.config
        st = self.node.config
        cnt = 0
        for idx in range(0, len(tg)):
            for i in range(0, min(len(st[idx]), len(tg[idx]))):
                if st[idx][i] != tg[idx][i]:
                    cnt += 1
            cnt += max(0, len(st[idx]) - len(tg[idx]))

        return cnt

    def __repr__(self):
        return str(self.node.config) + ", " + str(self.cost)


visited = []

if __name__ == '__main__':
    start_node = Node([["a"], ["b", "c"], ["d"]])
    target_node = Node([["c", "b"], [], ["a", "d"]])

    open_list = [PathNode(dp(start_node), 0, None)]
    visited = [PathNode(dp(start_node), 0, None)]

    while len(open_list) > 0:
        open_list.sort(key=lambda pth: pth.cost + pth.heuristic(target_node))
        current = open_list.pop(0)
        if current.node == target_node:
            print("success " + str(current.cost))
            it = current
            while True:
                print(it.node)
                if it.parent_node is None:
                    break
                it = it.parent_node
            break
        for nxt in current.node.expand():
            new_cost = current.cost + 1
            old_path_node = next((node for node in visited if node.node == nxt), None)

            if old_path_node is None:
                open_list.append(PathNode(nxt, new_cost, current))
                visited.append(PathNode(nxt, new_cost, current))
            else:
                if new_cost < old_path_node.cost:
                    open_list = open_list.filter(lambda x: x.node != old_path_node.node)
                    visited = visited.filter(lambda x: x.node != old_path_node.node)
                    open_list.append(PathNode(nxt, new_cost, current))
                    visited.append(PathNode(nxt, new_cost, current))
