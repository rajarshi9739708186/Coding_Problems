class Node:
    def __init__(self, data):
        self.NodeData = data
        self.NextNodePointer = None

class SingleLinkedList:
    # While we will create Linked list
    # Start Node pointer will be created
    # It suppose to point very first node of linked list
    def __init__(self):
        self.StartNodePointer = None

    # Traverse entire Linked List
    def traverseLinkedList(self):
        tempNodePointer = self.StartNodePointer  # Create a Temporary pointer, Using this will traverse List

        # If Linked List doesn't contain any node
        if self.StartNodePointer == None:
            print("Linked List is Empty")
        else:
            while tempNodePointer != None: # Till Last Node Traversal will be
                print(tempNodePointer.NodeData)
                tempNodePointer = tempNodePointer.NextNodePointer

    # Add a node at the end of the Linked List
    def addNodeAtLast(self, node_data):
        # Create Node
        New_Node = Node(node_data)

        # If Linked List doesn't contain any node
        if self.StartNodePointer == None:
            # As StartNodePointer is pointing to Nothing
            # Now it will point to created Node
            self.StartNodePointer = New_Node
        else:
            tempNodePointer = self.StartNodePointer  # Create a Temporary pointer, Using this will traverse List

            # Traverse till last node of the list
            while tempNodePointer.NextNodePointer != None:
                tempNodePointer = tempNodePointer.NextNodePointer

            # Now tempNodePointer is pointing to Last Pointer
            tempNodePointer.NextNodePointer = New_Node  # Last node of the existing list will be pointing to New Node. New Node becomes last

    # Find the middle element of Linked List
    def findMiddleOfLinkedList(self):
        slow_pointer = self.StartNodePointer # Will increment one step. 1, 2, 3, ...
        fast_pointer = self.StartNodePointer # Will increment two steps. 1, 3, 5, ...

        # While fast_pointer reaches at end, slow_pointer will be in middle
        # Ideally List contains atleast 3 node to find middle

        if self.StartNodePointer == None:
            print("Linked List is empty")
        elif self.StartNodePointer.NextNodePointer == None:
            print("List contain only one Node")
        elif self.StartNodePointer.NextNodePointer.NextNodePointer == None:
            print("List contain two Nodes")
        else:
            # List contains atleast 3 Nodes
            List_Contain_Even_Number_Nodes = False

            while fast_pointer.NextNodePointer != None:
                if fast_pointer.NextNodePointer.NextNodePointer == None:
                    # It means List have even number of Nodes
                    List_Contain_Even_Number_Nodes = True
                    fast_pointer = fast_pointer.NextNodePointer
                else:
                    fast_pointer = fast_pointer.NextNodePointer.NextNodePointer
                    slow_pointer = slow_pointer.NextNodePointer

            if List_Contain_Even_Number_Nodes:
                print(f"Middle nodes : {slow_pointer.NodeData} and {slow_pointer.NextNodePointer.NodeData}")
            else:
                print(f"Middle node : {slow_pointer.NodeData}")

SingleLinkedList_object = SingleLinkedList()

while True:
    print("")
    print("Press 1 to add data into Single Linked List")
    print("Press 2 to print Single Linked List")
    print("Press 3 to middle of Single Linked List")
    print("Press 4 to Quit operation")
    print("")

    user_choice = int(input("Enter your choice : ").strip())

    if user_choice == 1:
        data_to_be_added = int(input("data to be added : ").strip())
        SingleLinkedList_object.addNodeAtLast(data_to_be_added)
    if user_choice == 2:
        SingleLinkedList_object.traverseLinkedList()
    if user_choice == 3:
        SingleLinkedList_object.findMiddleOfLinkedList()
    if user_choice == 4:
        print("Bye")
        break