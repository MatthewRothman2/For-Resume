#GetNum by Matthew Rothman
#Python Methodologies
#Professor Sorenson

# This is a comment
#
#  Simple implementation of a singly linked list
#

class Node(object):

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

class linkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert(self, node):

        if not self.head:
            self.head = node
            self.size += 1
        else:
            # set new nodes pointer to old head
            node.nextNode = self.head
            # reset head to new node
            self.head = node
            self.size +=1

    def getSize(self):
        return self.size

    def printLL(self):
        mynode = self.head
        c = 0
        while mynode:
            c += 1
            print(mynode.data, c)
            mynode = mynode.nextNode

    def getNum(self,n):  #Define method
        first_pointer = self.head #create a varible that points to head
        second_pointer = self.head #create second variable that points to a head
        count = 0 #create counter
        while second_pointer and count  <= n: #while the second pointer and counter are less than n
            first_pointer = first_pointer.nextNode #move the first pointer to the next node
            count += 1 #add count
            

        while first_pointer and second_pointer:
            first_pointer = first_pointer.nextNode #first pointer get count of nodes
            second_pointer = second_pointer.nextNode #second pointer can print the stored numbered nodes
        print(second_pointer.data)

        

    
            



            

    

        

 
