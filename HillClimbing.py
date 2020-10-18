#Defining a class for every node of the tree - 
#Each Node has two members: Data and the Heuristic value of the Node.
class Node:
    def __init__(self, data, heu):
        self.left = None
        self.right = None
        self.heu = heu
        self.data = data


#Insert Function to insert a node in the tree
def insert(root, parent, data, dir, heu):
    #Searching for the parent node
    x = search(root, parent)
    #insert the current node as a left or right child based on dir
    if dir==0:
        x.left = Node(data, heu)
    else:
        x.right = Node(data, heu) 

#Function to search for the parent node using LEVEL ORDER search
def search(node, parent):
    queue = list()
    queue.append(node)
    while(len(queue)):
        node = queue[0]
        queue.pop(0)
        if(node.data==parent):
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return

#Function implementing the Hill Climbing algorithm (minimizing heuristics)
def HillClimbing(root, goal):
    op = []
    cl = []
    current = root
    op.append(current)
    while(len(op)!=0):
        current = op.pop(0)
        if(current.left!=None):
            op.append(current.left)
        if(current.right!=None):
            op.append(current.right)

        #sorting to select the node with minimum heuristic value in the next turn
        op.sort(key = lambda c: c.heu)
        cl.append(current.data)
        #terminating once we reach the goal state
        if(current.data==goal):
            break
    return cl

#Driver Code
if __name__ == "__main__":
    n = int(input("Enter the total no. of nodes in the tree: "))
    x = input("Enter the root node and its heuristic value: ").split()
    root = Node('S', 0)
    n-=1
    while n:
        x = input("Enter the Parent Node, Current Node, Left(0)/Right(1), Heuristic: ").split()
        insert(root, x[0], x[1], int(x[2]), int(x[3]))
        n-=1
    goal = input("Enter the goal state: ")

    result = HillClimbing(root, goal)
    
    #printing the path from root to the goal node
    print("\nThe path from Root to Goal node is : \n")
    for i in range(len(result)-1):
        print(result[i], " - ", end="")
    print(result[len(result)-1])
    print()


    
    

