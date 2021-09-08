# program #1
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def accept_data(self, data):
        new_node = Node(data);
        cur = self.head;
        while cur.next != None:
            cur = cur.next
            cur.next = new_node
    
    def display(self):
        disp = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            disp.append(cur.data)
        
        print(disp)


l = LinkedList();
l.accept_data(1)
l.accept_data(2)
l.display()



# program #2


       
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
class SLinkedList:
   def __init__(self):
      self.headval = None
# Function to add newnode
   def AtEnd(self, newdata):
      NewNode = Node(newdata)
      if self.headval is None:
         self.headval = NewNode
         return
      laste = self.headval
      while(laste.nextval):
         laste = laste.nextval
      laste.nextval=NewNode
# Print the linked list
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.AtEnd("Thu")

list.listprint()