from copy import deepcopy as dp
from timeit import default_timer as timer

f = open("output.txt", "w+")
KEY_LENGTH = 7
keys = []
input_files = [
    'input1.txt',  # solution has length 7
    'input2.txt',  # solution has length 3
    'input3.txt',  # good heuristic gives length 6, bad one length 7
    'input4.txt',  # no solution
]


def convert_key(key):
    key_lst = []
    for ch in key:
        if ch == 'i':
            key_lst.append(-1)
        elif ch == 'd':
            key_lst.append(1)
        else:
            key_lst.append(0)

    return key_lst


def convert_key_back(key_lst):
    key = '['
    for i, val in enumerate(key_lst):
        if val == -1:
            key = key + 'i'
        elif val == 1:
            key = key + "d"
        else:
            key = key + 'g'

        if i != len(key_lst) - 1:
            key = key + ','

    key = key + ']'

    return key


class Node:
    def __init__(self, config):
        self.config = config

    def successors(self):
        node_cpy = dp(self.config)
        config_lst = []

        for i, key in enumerate(keys):
            new_config = dp(node_cpy)

            for j, x in enumerate(key):
                new_config[j] += x
                new_config[j] = min(new_config[j], 0)

            config_lst.append(Node(new_config))

        return config_lst

    def __eq__(self, other):
        return self.config == other.config

    def __repr__(self):
        ans = '['
        for i, val in enumerate(self.config):
            if val == 0:
                ans = ans + 'inc(d, 0)'
            else:
                ans = ans + 'inc(i, {})'.format(-val)

            if i != len(self.config) - 1:
                ans = ans + ', '

        ans = ans + ']'
        return ans


class PathNode:
    Type = 1

    def __init__(self, node, cost, parent_node):
        self.node = node
        self.cost = cost
        self.parent_node = parent_node

    def is_final(self, target):
        lst = [x for x in self.node.config if x in target.config]
        return len(lst) == KEY_LENGTH

    def heuristic1(self):  # good heuristic
        return -min(self.node.config)

    def heuristic2(self):  # good heuristic
        return -min(self.node.config) + max(self.node.config)

    def heuristic3(self):  # bad heuristic
        return 2 * -sum(self.node.config)

    def heuristic(self):
        if PathNode.Type == 1:
            return self.heuristic1()
        if PathNode.Type == 2:
            return self.heuristic2()
        if PathNode.Type == 3:
            return self.heuristic3()

    def recursive_print(self):
        if self.parent_node is None:
            return

        self.parent_node.recursive_print()
        key = convert_key_back([self.node.config[i] - self.parent_node.node.config[i] for i in range(KEY_LENGTH)])
        print_to_file("We use key: {} to get to lock configuration: {}".format(key, self.node))

    def print_path(self):
        print_to_file("Nr of moves: " + str(self.cost))
        print_to_file("Initial state: {}".format(Node([-1 for i in range(KEY_LENGTH)])))
        self.recursive_print()

    def __repr__(self):
        return str(self.node.config) + ", " + str(self.cost)


visited = []


def read_keys_file(file_name):
    with open(file_name, "r") as fin:
        for line in fin.readlines():
            keys.append(convert_key(line[:-1]))


def print_to_file(output):
    f.write(output + '\n')


if __name__ == '__main__':
    start = timer()

    PathNode.Type = 1
    fileName = input_files[2]
    print_to_file("We read from {} file".format(fileName))
    read_keys_file(fileName)
    KEY_LENGTH = len(keys[0])

    start_node = Node([-1] * KEY_LENGTH)
    target_node = Node([0] * KEY_LENGTH)

    open_list = [PathNode(dp(start_node), 0, None)]
    visited = [PathNode(dp(start_node), 0, None)]

    solution_flag = False
    while len(open_list) > 0:
        open_list.sort(key=lambda pth: pth.cost + pth.heuristic())
        current = open_list.pop(0)
        if current.is_final(target_node):
            solution_flag = True
            current.print_path()
            break

        for nxt in current.node.successors():
            # we check if successor is useless
            delta = max([nxt.config[i] - current.node.config[i] for i in range(KEY_LENGTH)])
            if delta != 1:
                # if delta != 1 ---> no lock level has improved
                continue

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

    if not solution_flag:
        print_to_file("No solution for this keys configuration")

    end = timer()
    print_to_file('Program executed for {} seconds.'.format(end - start))
