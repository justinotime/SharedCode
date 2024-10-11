class OceanNode:
    def __init__(self, animal=set(), left=None, right=None):
        self.animal = animal
        self.left = left
        self.right = right

def ocean_explore(node, search_animals):
    # Helper function to traverse the tree and track depth
    def explore_depth(node, search_animals, depth):
        if node is None:
            return (False, 0)
        # Check if search_animals is a subset of current node's animals
        if search_animals.issubset(node.animal):
            return (True, depth)
        # Recursively check the left and right children
        left_result = explore_depth(node.left, search_animals, depth + 1)
        if left_result[0]:
            return left_result

        return explore_depth(node.right, search_animals, depth + 1)
    return explore_depth(node, search_animals, 0)