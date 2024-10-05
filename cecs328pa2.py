class OceanNode:
    def __init__(self, animal=set(), left=None, right=None):
        self.animal = animal
        self.left = left
        self.right = right
def ocean_explore(area, animal_set):
    def search(area, animal_set, depth):
        if area is None:
            return False, depth
        if animal_set <= area.animal:
            return True, depth
            
        found_left, left_depth = search(area.left, animal_set, depth+1)
        found_right, right_depth = search(area.right, animal_set, depth+1)
        
        if found_left and found_right:
            if left_depth < right_depth:
                return found_left, left_depth
            else:
                return found_right, right_depth
        elif found_left:
            return found_left, left_depth
        elif found_right:
            return found_right, right_depth
        else:
            return False, depth
    return search(area, animal_set, 0)
def main():
    area = OceanNode({"mako shark","blue whale"}, OceanNode({"krill","angelfish","zebra fish"}, None,
           OceanNode({"squid","sand shark"}, OceanNode({"eel","manta ray","lemon shark"},None,None), None)),
           OceanNode({"squid","lemon shark"}, None, None))
    print(ocean_explore(area,{"mako shark"}))
    print(ocean_explore(area,{"squid"}))
main()