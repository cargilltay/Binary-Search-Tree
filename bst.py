import networkx as nx

class Vertex:

    #contructor for Vertex
    def __init__(self, int_val, left = None, right = None):
        self.int_val = int_val
        self.left = left
        self.right = right


def add_node(val, node, g):
  
  #check if value is less than nodes value
  if(val < node.int_val):

    #go to left node
    if(node.left != None):
      add_node(val, node.left, g)
  
    #add node as left child
    else:
      g.add_edge(val, node.int_val)
      node.left = Vertex(val)
  
  #must be greater than node
  else:
  
    #go to right node
    if(node.right != None):
      add_node(val, node.right, g)
    
    #add node as right child
    else:
      g.add_edge(val, node.int_val)
      node.right = Vertex(val)
      

def simple_bst(int_list):
  
  g = nx.Graph();

  #add root to tree
  root = Vertex(int_list.pop(0))
  g.add_node(root.int_val)

  #add nodes appropriatly
  for i in int_list:
    add_node(i, root, g)

  #convert list to dict
  cust_d = {}
  for e in g.edges():
      cust_d[e[0]] = []
      cust_d[e[1]] = []

  for e in g.edges():
    key = e[0]
    value = e[1]

    #append to dictionary lists
    cust_d[key].append(value)
    cust_d[value].append(key)
  
  #return dictionary of tree
  return cust_d

print simple_bst([5,0,3,9,10,4,11,2])
