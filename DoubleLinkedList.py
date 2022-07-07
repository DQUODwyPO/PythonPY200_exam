from typing import Iterator, Any, Iterable, Optional
from collections.abc import MutableSequence

from DoubleLinkedNode import Node, DoubleLinkedNode


class LinkedList(MutableSequence):

    def __init__(self, data: Iterable = None):
        super().__init__()
        self.__len = 0
        self.__head: Optional[DoubleLinkedNode] = None
        self.__tail: Optional[DoubleLinkedNode] = None
        if data is not None:
            for elem in data:
                self.append(elem)

    def get_item(self, index) -> DoubleLinkedNode:
        if not isinstance(index, int):
            raise TypeError("Index is not int")
        if index == -1:
            return self.__tail
        node = self.__head
        for _ in range(index):
            node = node.next
        return node

    def __getitem__(self, item: int) -> DoubleLinkedNode:
        if not isinstance(item, int):
            raise TypeError("Item is not int")

        if not -1 <= item < self.__len:
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

        node = DoubleLinkedNode(value)
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
        node = DoubleLinkedNode(value)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node
            self.__tail = node
        self.__len += 1


class DoubleLinkedList(LinkedList):

    def __init__(self, data: Iterable = None):
        super().__init__(data)
        self.prevers()

    def prevers(self):
        len_ = super().__len__()
        past = super().__getitem__(0)
        elem = super().__getitem__(1)
        for _ in range(len_ - 1):
            elem.prev = past
            past = elem
            elem = elem.next

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Key is not int")

        if not 0 <= key < super().__len__():
            raise IndexError("Index is not in range(len)")

        last = None
        if key < super().__len__() - 1:
            last = super().__getitem__(key + 1)
        last.prev = None
        super().__delitem__(key)

    def __repr__(self):
        str_ = f"DoubleLinkedList(["
        node = super().__getitem__(0)
        for i in range(super().__len__() - 1):
            str_ += f"{node.value}, "
            node = node.next
        str_ += f"{super().__getitem__(-1)}])"
        return str_

    def insert(self, index: int, value: int) -> None:
        super().insert(index, value)
        node0 = None
        node1 = super().__getitem__(index)
        node2 = node1.next
        if node2 is not None:
            node2.prev = node1
        if index > 0:
            node0 = super().__getitem__(index - 1)
        node1.prev = node0

    def append(self, value: int) -> None:
        super().append(value)
        len__ = super().__len__()
        if len__ > 1:
            first = super().__getitem__(len__ - 2)
            last = super().__getitem__(len__ - 1)
            last.prev = first
