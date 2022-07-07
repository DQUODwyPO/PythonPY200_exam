from typing import Iterator, Any, Iterable, Optional
from collections.abc import MutableSequence

from DoubleLinkedNode import Node


class LinkedList(MutableSequence):

    def __init__(self, data: Iterable = None):
        super().__init__()
        self.__len = 0
        self.__head: Optional[Node] = None
        self.__tail: Optional[Node] = None
        if data is not None:
            for elem in data:
                self.append(elem)

    def get_item(self, index) -> Node:
        if not isinstance(index, int):
            raise TypeError("Index is not int")
        node = self.__head
        for _ in range(index):
            node = node.next
        return node

    def __getitem__(self, item: int) -> Node:
        if not isinstance(item, int):
            raise TypeError("Item is not int")

        if not 0 <= item < self.__len:
            raise IndexError("Index is not in range(len)")
        return self.get_item(item)

    def __setitem__(self, key: int, value: int):
        if not isinstance(key, int):
            raise TypeError("Key is not int")

        if not isinstance(value, int):
            raise TypeError("Value is not int")

        if not 0 <= key < self.__len:
            raise IndexError("Index is not in range(len)")

        node = self.get_item(key)
        node.value = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Key is not int")

        if not 0 <= key < self.__len:
            raise IndexError("Index is not in range(len)")

        if key == 0:
            self.__head = self.__head.next
        elif key == self.__len - 1:
            node1 = self.get_item(key - 1)
            self.__tail = node1
            self.__tail.next = None
        else:
            node1 = self.get_item(key - 1)
            node2 = node1.next.next
            node1.next = node2

        self.__len -= 1
        if self.__len == 0:
            self.__tail = None

    def __len__(self):
        return self.__len

    def __str__(self):
        str_ = f"["
        node = self.__head
        for i in range(self.__len - 1):
            str_ += f"{node.value}, "
            node = node.next
        str_ += f"{self.__tail.value}]"
        return str_

    def __repr__(self):
        str_ = f"LinkedList(["
        node = self.__head
        for i in range(self.__len - 1):
            str_ += f"{node.value}, "
            node = node.next
        str_ += f"{self.__tail.value}])"
        return str_

    def insert(self, index: int, value: int) -> None:
        if not isinstance(index, int):
            raise TypeError("Index is not int")

        if not isinstance(value, int):
            raise TypeError("Value is not int")

        if not 0 <= index:
            raise IndexError("Index < 0")

        node = Node(value)
        if index == 0:
            node.next = self.__head
            self.__head = node
        elif index >= self.__len:
            self.__tail.next = node
            self.__tail = node
        else:
            node1 = self.get_item(index - 1)
            node2 = node1.next
            node1.next = node
            node.next = node2

        self.__len += 1

    def append(self, value: int) -> None:
        node = Node(value)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node
            self.__tail = node
        self.__len += 1


class DoubleLinkedList(LinkedList):
    ...

