class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next_node=next
class single_linked_list:
    def __init__(self) -> None:
        self.root=None
        self.length=-1
    def insert_at_start(self,data):
        new_loc=Node(data,self.root)
        self.root=new_loc
        self.length+=1
    def insert_at_end(self,data):
        if self.root is None:
            self.root=Node(data,None)
            self.length+=1
            return
        temp=self.root
        while temp.next_node:
            temp=temp.next_node
        temp.next_node=Node(data,None)
        self.length+=1
    def lilength(self):
        print("length of linked list is",self.length+1)
        
    def display(self):
        if self.root is None:
               print("Empty")
               return
        root=self.root
        while root:
                print(root.data)
                root=root.next_node
    def addvalues(self,data):
        for i in data:
            self.insert_at_end(i)
    def remove(self,index):
        if index<0 or index>self.length:
            raise IndexError("Invalid index as %s"% index)
            return
        


li=single_linked_list()
li.insert_at_start(9)
li.insert_at_start(8)
li.insert_at_end(10)
li.insert_at_end(11)
li.insert_at_end(12)
li.addvalues([1,2,3,4,5,6,7])
li.lilength()
li.display()