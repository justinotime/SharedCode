class OceanNode:
    def __init__(self, animal=set(), left = None, right = None):
        self.animal = animal
        self.left = left
        self.right = right

def ocean_explore(node = set(), search_animals = ""):
    # Helper Function 
    def explore_Depth(node, search_animals, depth):
        # Base Case
        if node is None:
            return (False, 0)
        # 
        if search_animals.issubset(node.animal):
            return(True, depth)
        # Transvering through the left side of the node, and then right
        left = explore_Depth(node.left, search_animals, depth + 1)
        right = explore_Depth(node.right, search_animals, depth + 1)

        if left[0]:
            return left
        elif right[0]:
            return right
        else:
            return (False, 0)
    return explore_Depth(node, search_animals, 0)


area = OceanNode({"mako shark", "blue whale"}, # Root node
    OceanNode({"krill", "angelfish", "zebra fish"}, None, # Left Node
    OceanNode({"squid", "sand shark"}, 
    OceanNode({"eel", "manta ray", "lemon shark"}, None, None), None)),
    OceanNode({"squid", "lemon shark"}, None, None)) # Right node


ocean_explore(area, {"Fish"})