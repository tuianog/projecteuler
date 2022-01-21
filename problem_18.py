
class Node:
    def __init__(self, value: int):
        self.value = value
        self.left_child = None
        self.right_child = None
    
    def set_left_child(self, value: int):
        self.left_child = Node(value)

    def set_right_child(self, value: int):
        self.right_child = Node(value)

    def __str__(self) -> str:
        return f'Value: {self.value} Left: {self.left_child.value} Right: {self.right_child.value}'


def build_tree():
    lvls = [
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    ]

    nodes = []
    for v in lvls[0]:
        nodes.append(Node(v))
    
    for i in range(1, len(lvls)):
        lvl_nodes = []
        for j in range(len(lvls[i])):
            node = Node(lvls[i][j])
            node.set_left_child(lvls[i-1][j])
            node.set_right_child(lvls[i-1][j+1])
            print(node)
            lvl_nodes.append(node)
        nodes.append(lvl_nodes)
        


if __name__ == "__main__":
    root = build_tree()