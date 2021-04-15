class node:
    def __init__(self,data):
        self.data=data
        self.nref=None   #next ref 
        self.pref=None   #prev ref

class doubly_LL:
    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head==None:
            print("Linked List is empty")
        else:
            n=self.head
            while n!=None:
                print(n.data)
                n=n.nref

    def print_LL_reverse(self):
        if self.head==None:
            print("Linked List is empty")
        else:
            n=self.head
            while n.nref!=None:   #used n.nref becoz we want to use the last node
                n=n.nref          #here n is last node
            while n!=None:
                print(n.data)
                n=n.pref

    def insert_begin(self,data):
        new_node=node(data)
        if self.head==None:
            print("Linked List was empty")
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node #have to also consider the initial first node 
            new_node.pref=None
            self.head=new_node

    def insert_end(self,data):
        new_node=node(data)
        if self.head==None:
            print("Linked List is empty")
            self.head=new_node
        else:
            n=self.head
            while n.nref!=None:      #going to the last node(n)
                n=n.nref
            new_node.nref=None
            new_node.pref=n
            n.nref=new_node

    def insert_after_node(self,data,x):
        new_node=node(data)
        if self.head==None:
            print("Linked List is empty")
            self.head=new_node
        else:
            n=self.head
            while n.nref!=None:
                if n.data==x:
                    break
                else:
                    n=n.nref
            if n.nref==None:
                print("Node not found in Linked List")
            else:
                new_node.nref=n.nref
                new_node.pref=n
                n.nref=new_node

    def insert_before_node(self,data,x):
        new_node=node(data)
        if self.head==None:
            print("Linked List is empty")
        else:
            n=self.head
            while n!=None:
                if n.data==x:
                    break
                else:
                    n=n.nref
            if n==None:
                print("Given Node not found in Linked List")
            else:
                new_node.pref=n.pref
                new_node.nref=n
                #if u r trying to insert before first node
                if n.pref!=None:
                    n.pref.nref=new_node
                else:
                    self.head=new_node
                    n.pref=new_node

    def delete_begin(self):
        if self.head==None:
            print("Linked List is empty")
        elif self.head.nref==None:
            print("Linked List contains only one node")
            self.head=None
        else:
            n=self.head
            n.nref.pref=None
            self.head=n.nref

    def delete_end(self):
        if self.head==None:
            print("Linked List is empty")
        elif self.head.nref==None:
            print("Linked List contains only one node")
            self.head=None
        else:
            n=self.head
            while n.nref!=None:
                n=n.nref
            n.pref.nref=None

    def delete_node_by_value(self,x):
        if self.head==None:
            print("Linked List is empty")
        elif self.head.nref==None:
            print("Linked List contains only one node")
            self.head=None
        else:
            n=self.head
            while n.nref!=None:
                if n.data==x:
                    break
                else:
                    n=n.nref
            if n==None:
                print("Node not present in Linked List")
            else:
                n.pref.nref=n.nref
                n.nref.pref=n.pref





                    


dL1=doubly_LL()
dL1.insert_begin(10)
dL1.insert_begin(20)
dL1.insert_end(30)
dL1.insert_end(35)
dL1.insert_after_node(40,10)
dL1.insert_before_node(50,20)
dL1.delete_begin()
dL1.delete_end()
dL1.delete_node_by_value(10)
dL1.print_LL()



                


            



            
