class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.n = 0

    def display(self):
        curr = self.head
        while curr!= None:
            print(curr.data)
            curr = curr.next

# _______________________________________Insert Operation______________________________

    def insert_from_tail(self,value):
        if self.head == None:
            new_node = Node(value)
            self.head =  new_node
        else:
            new_node = Node(value)
            curr = self.head
            while curr.next != None:
                curr = curr.next
            
            curr.next = new_node
            self.n += 1

    def insert_from_head(self,value):
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.n +=1
        
    def insert_after_data(self,data,value):
        
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == data:
                break
            else:
                curr = curr.next
        
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return "Item Not found"

    def insert_before_data(self, data, value):
        new_node = Node(value)
        curr = self.head
        prev = None
        
        while curr is not None:
            if curr.data == data:
                break
            prev = curr
            curr = curr.next

        if curr is not None:
            new_node.next = curr
            if prev is not None:
                prev.next = new_node
            else:
                self.head = new_node
            self.n += 1
        else:
            return "Item Not found"

# _______________________________________Delete Operation______________________________

    def delete_all(self):
        self.head = None
        self.n = 0

    def delete_from_tail(self):
        curr = self.head
        while curr.next.next != None:
            curr = curr.next
        
        curr.next = None
        self.n -=1

    def delete_from_head(self):
        if self.head == None:
            return None
        else:
            curr = self.head.next
            self.head =  curr
            self.n -=1
            
    def delete_from_data(self,data):
        curr = self.head
        while curr.next != None:
            if curr.next.data == data:
                break
            curr = curr.next
        
        if curr.next == None:
            return "Not found"
        else:
            curr.next = curr.next.next

            
            
            
    
l = LinkedList()
l.insert_from_tail(1)
l.insert_from_head(2)
l.insert_from_head(3)
l.insert_from_head(4)
l.insert_from_head(5)

l.insert_before_data(3,30)

l.delete_from_data(3)


l.display()