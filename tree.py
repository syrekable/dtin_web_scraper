from typing import Union

class Tree:
    '''
        a class representing an undirected graph with no cycles
    '''
    existing_nodes = [] ##cycle protection
    
   
    def __init__(self, name: str, graph_dict_keys: Union[list, None]):
        self.name = name
        if graph_dict_keys is not None:
            self._graph_dict = {k:{} for k in graph_dict_keys}
        else:
            self._graph_dict = {"directs": "nowhere"}
    
    @staticmethod
    def mark_visited(url):
        Tree.existing_nodes.append(url)



    def add_node(self, node):
        '''
            adds a new node to the graph iff it hasn't been already
            added by any of the other nodes
        '''
        if node.name not in self._graph_dict.keys():
            Tree.existing_nodes.append(node.name)
            self._graph_dict[node.name] = node._graph_dict


    def print_nodes(self, branch=None, depth=None):
        '''
            a recursive procedure printing nodes of a branch in a tree fashion
	'''
        if branch is None:
            print("{}:".format(self.name))
            branch = self._graph_dict
        if depth is None:
            depth = 1

        for k,v in branch.items():
            if isinstance(v, dict):
                print("{}{}:".format(depth*"  ", k))
                self.print_nodes(branch=v, depth=depth+1)
            else:
                print("{}|--{}\n".format((depth+1)*"  ", v))
