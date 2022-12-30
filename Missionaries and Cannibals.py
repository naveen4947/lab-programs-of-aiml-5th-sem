import copy

class CoastState:
    def __init__(self, c, m):

        self.cannibals = c
        self.missionaries = m
# This is an intermediate state of Coast where the missionaries have to outnumber the cannibals

    def valid_coast(self):
        if self.missionaries >= self.cannibals or pself.missionaries == 0:
            return True
        else:
            return False


    def goal_coast(self):
        if self.cannibals == 3 and self.missionaries == 3:
            return True
        else:
            return False


class GameState:
    def __init__(self, data):
        self.data = data
        self.parent = None

# Creating the Search Tree

    def building_tree(self):
        children = []
        coast = ""
        across_coast = ""
        temp = copy.deepcopy(self.data)
        if self.data["boat"] == "left":
            coast = "left"
            across_coast = "right"
        elif self.data["boat"] == "right":
            coast = "right"
            across_coast = "left"

        # MOVING 2 CANNIBALS (CC)
        if temp[coast].cannibals >= 2:
            temp[coast].cannibals = temp[coast].cannibals - 2
            temp[across_coast].cannibals = temp[across_coast].cannibals + 2
            temp["boat"] = across_coast
            if temp[coast].valid_coast() and temp[across_coast].valid_coast():
                child = GameState(temp)
                child.parent = self
                children.append(child)

        temp = copy.deepcopy(self.data)

        # MOVING 2 MISSIONARIES (MM)
        if temp[coast].missionaries >= 2:
            temp[coast].missionaries = temp[coast].missionaries - 2
            temp[across_coast].missionaries = temp[across_coast].missionaries + 2
            temp["boat"] = across_coast
            if temp[coast].valid_coast() and temp[across_coast].valid_coast():
                child = GameState(temp)
                child.parent = self
                children.append(child)

        temp = copy.deepcopy(self.data)

        # MOVING 1 CANNIBAL (C)
        if temp[coast].cannibals >= 1:
            temp[coast].cannibals = temp[coast].cannibals - 1
            temp[across_coast].cannibals = temp[across_coast].cannibals + 1
            temp["boat"] = across_coast
            if temp[coast].valid_coast() and temp[across_coast].valid_coast():
                child = GameState(temp)
                child.parent = self
                children.append(child)

        temp = copy.deepcopy(self.data)

        # MOVING 1 MISSIONARY (M)
        if temp[coast].missionaries >= 1:
            temp[coast].missionaries = temp[coast].missionaries - 1
            temp[across_coast].missionaries = temp[across_coast].missionaries + 1
            temp["boat"] = across_coast
            if temp[coast].valid_coast() and temp[across_coast].valid_coast():
                child = GameState(temp)
                child.parent = self
                children.append(child)

        temp = copy.deepcopy(self.data)

        # MOVING 1 CANNIBAL AND 1 MISSIONARY (CM && MM)
        if temp[coast].missionaries >= 1 and temp[coast].cannibals >= 1:
            temp[coast].missionaries = temp[coast].missionaries - 1
            temp[across_coast].missionaries = temp[across_coast].missionaries + 1
            temp[coast].cannibals = temp[coast].cannibals - 1
            temp[across_coast].cannibals = temp[across_coast].cannibals + 1
            temp["boat"] = across_coast
            if temp[coast].valid_coast() and temp[across_coast].valid_coast():
                child = GameState(temp)
                child.parent = self
                children.append(child)
        return children


def breadth_first_search():
    left = CoastState(3, 3)
    right = CoastState(0, 0)
    root_data = {"left": left, "right": right, "boat": "left"}
    explored = []
    nodes = []
    path = []
    while len(nodes) > 0:
        g = nodes.pop(0)
        explored.append(g)
        if g.data["right"].goal_coast():
            path.append(g)
            return g
        else:
            next_children = g.building_tree()
            for x in next_children:
                if (x not in nodes) or (x not in explored):
                    nodes.append(x)
    return None


def print_path(g):
    path = [g]
    while g.parent:
        g = g.parent
        path.append(g)
    print("\n\t\t      Left Side\t\t|     Right Side\t   |   Boat")
    print("\t\tCannibals Missionaries\t| Cannibals Missionaries   | Position\n")
    counter = 0
    for p in reversed(path):
        print(f'Step  {counter} \tLeft C: {p.data["left"].cannibals}. Left M: {p.data["left"].missionaries}.   | Right C: {p.data["right"].cannibals}. Right M: {p.data["right"].missionaries}.  | Boat: {p.data["boat"]}')
        counter = counter + 1
    print("\n\nEnd of Path!\n\n")


def main():
    solution = breadth_first_search()
    print("Missionaries and Cannibals AI Problem Solution using Breath - First Search:")
    print_path(solution)

if __name__ == '__main__':
    main()
