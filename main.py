class OceanNode:
    def __init__(self, animal=set(), left = None, right = None):
        self.animal = animal
        self.left = left
        self.right = right

def ocean_explore(node = set(), search_animals = None):
    # if search_animals in node or node is not set():
    # base case should test if the set (node) is not a set then return false Immediately
    if type(node) 
        return False
    else:
        return True


area = OceanNode({"mako shark", "blue whale"}, # Root node
    OceanNode({"krill", "angelfish", "zebra fish"}, None, # Left Node
    OceanNode({"squid", "sand shark"}, 
    OceanNode({"eel", "manta ray", "lemon shark"}, None, None), None)),
    OceanNode({"squid", "lemon shark"}, None, None)) # Right node

area2 = OceanNode(None,None,None)


ocean_explore(area,{"mako shark"})
ocean_explore(area2,{"mako shark"})
