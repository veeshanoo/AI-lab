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
            col = pos % 3

            if col == 2 and add == 1:
                continue
            if col == 0 and add == -1:
                continue

            if -1 < new_pos < 9:
                nxt_config = dp(node_cpy)
                nxt_config[pos], nxt_config[new_pos] = nxt_config[new_pos], nxt_config[pos]

                config_lst.append(Node(nxt_config))

        return config_lst

    def __eq__(self, other):
        return self.config == other.config

    def __repr__(self):
        return str(str(self.config[:3]) + "\n" + str(self.config[3:6]) + "\n" + str(self.config[6:]))


class PathNode:
    def __init__(self, node, cost, parent_node):
        self.parent_node = parent_node
        self.node = node
        self.cost = cost

    def heuristic(self, target):
        st = self.node.config
        tg = target.config
        cnt = 0

        for id1, el1 in enumerate(st):
            for id2, el2 in enumerate(tg):
                if el1 == el2:
                    col1 = id1 % 3
                    line1 = id1 // 3
                    col2 = id2 % 3
                    line2 = id2 // 3

                    cnt += abs(col1 - col2) + abs(line1 - line2)

        return cnt

    def __repr__(self):
        return str(self.node.config) + ", " + str(self.cost)


visited = []

if __name__ == '__main__':
    # start_node = Node([5, 7, 2, 8, 0, 6, 3, 4, 1])
    start_node = Node([6, 8, 5, 1, 0, 2, 7, 4, 3])
    target_node = Node([1, 2, 3, 4, 5, 6, 7, 8, 0])

    # We should check inversion parity, if odd -> no solution
    inv_cnt = 0
    for id1, el1 in enumerate(start_node.config):
        for id2, el2 in enumerate(start_node.config):
            if id1 < id2 and el1 > el2 > 0:
                inv_cnt += 1

    if inv_cnt % 2 == 1:
        print("No solution")
    else:
        open_list = [PathNode(dp(start_node), 0, None)]
        visited = [PathNode(dp(start_node), 0, None)]

        # steps = 0
        while len(open_list) > 0:
            # steps += 1
            # pp(steps)
            # pp(open_list)
            open_list.sort(key=lambda pth: pth.cost + pth.heuristic(target_node))
            current = open_list.pop(0)
            if current.node == target_node:
                print("Nr of moves: " + str(current.cost))
                it = current
                while True:
                    print(it.node)
                    print()
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
                        # pp(open_list)
                        open_list = [x for x in open_list if x.node != old_path_node.node]
                        visited = [x for x in visited if x.node != old_path_node.node]
                        open_list.append(PathNode(nxt, new_cost, current))
                        visited.append(PathNode(nxt, new_cost, current))
