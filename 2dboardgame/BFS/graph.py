class Node:
   def __init__(self,val):
       self.value = val
       self.edges = []

   def set_value(self, val):
       self.value = val

   def get_value(self):
       return self.value

   def get_edges(self):
       return self.edges

   def __str__(self):
       return "Node with value " + str(self.value)

class Graph:
   def __init__(self):
       self.nodes = []

   def get_nodes(self):
       return self.nodes

   def add_node(self,n):
       if n in self.nodes:
           raise ValueError('Node already exists')
       self.nodes.append(n)

   def add_edge(self, n1, n2):
       if self.edge_exists(n1, n2):
           raise ValueError('Node already exists.')
       n1.edges.append(n2)
       n2.edges.append(n1)

   def __str__(self):
       s = "Graph with the following nodes:"
       for n in self.get_nodes():
           s += "\n\t" + str(n)
       return s

   def edge_exists(self, n1, n2):
       if n1 in n2.edges:
           return True
       else:
           return False


   def find_node(self, v):

        # Given a value v, this method returns the node in the graph that has value v.
        # This method is useful for building the hyperlanes from the provided list.
        for n in self.get_nodes():
            if n.get_value() == v:
                return n
        raise ValueError("Node not found.")

