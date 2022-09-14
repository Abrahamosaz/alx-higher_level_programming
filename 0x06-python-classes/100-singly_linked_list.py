#!/usr/bin/python3

"""creating a class Node"""


class Node:
    """Define a node of a single linked list"""

    def __init__(self, data, next_node=None):
        """initialise a instance of the class Node
        Args:
            data (int): data to be stored int the linked list
            next_node (Node instance): hold the address of the next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """function to retrive the data of the linked lsit data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if (type(value) != int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """function to retrive the address of the next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """"class to create instances of single linked list"""

    def __init__(self):
        """initialize a instance of the class SingleLinkedList"""

        self.__head = None

    def sorted_insert(self, value):
        """add a value to a node instance and sort the linked list"""

        new = Node(value)

        if self.__head is None:
            self.__head = new
        elif self.__head.data > new.data:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """string representation of the class instances"""

        values = []
        temp = self.__head
        while (temp is not None):
            values.append(str(temp.data))
            temp = temp.next_node
        return ("\n".join(values))
