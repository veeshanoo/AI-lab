from copy import deepcopy as dp
from pprint import pprint as pp


class Node:
    def __init__(self, config):
        self.config = config

    def expand(self):
        node_cpy = dp(self.config)
        config_lst = []

        pos = 0
        for i in range(9):
            if node_cpy[i] == 0:
                pos = i
                break

        for add in [-3, -1, 1, 3]:
            new_pos = pos + add
            if new_pos > -1 and new_pos < 9:
                nxt_config = dp(config_lst)
                nxt_config[pos], nxt_config[new_pos] = nxt_config[new_pos], nxt_config[pos]

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

    def heuristic(self):
        st = self.node.config
        cnt = 0



        return cnt

    def __repr__(self):
        return str(self.node.config) + ", " + str(self.cost)


visited = []

if __name__ == '__main__':
    start_node = Node([5, 7, 2, 8, 0, 6, 3, 4, 1])
    target_node = Node([1, 2, 3, 4, 5, 6, 7, 8, 0])

    open_list = [PathNode(dp(start_node), 0, None)]
    visited = [PathNode(dp(start_node), 0, None)]

    while len(open_list) > 0:
        open_list.sort(key=lambda pth: pth.cost + pth.heuristic())
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
            pp(nxt)
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