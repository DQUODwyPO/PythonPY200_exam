from typing import Iterator, Any, Iterable, Optional


class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value_: int, next_: Optional["Node"] = None):
        self.value = value_
        self.next = next_

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def is_valid(self) -> bool:
        if not isinstance(self.next, (self.__class__, None)):
            raise TypeError("Next Node is not Node or None type")

        if not isinstance(self.value, int):
            raise TypeError("Value is not int")

        return True


class DoubleLinkedNode(Node):
    ...

