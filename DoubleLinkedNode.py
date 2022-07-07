from typing import Iterator, Any, Iterable, Optional


class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value_: int, next_: Optional["Node"] = None):
        self.value = value_
        self.next_ = None
        self.next = next_

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    @property
    def next(self) -> Optional["Node"]:
        return self.next_

    @next.setter
    def next(self, next_: Optional["Node"] = None):
        self.is_valid(next_)
        self.next_ = next_

    @staticmethod
    def is_valid(node: Optional["Node"]) -> bool:
        if not isinstance(node, (Node, type(None))):
            raise TypeError("Node is not Node or None type")

        if node is not None:
            if not isinstance(node.value, int):
                raise TypeError("Value is not int")

        return True


class DoubleLinkedNode(Node):

    def __init__(self, value_: int, next_: Optional[Node] = None, prev_: Optional[Node] = None):
        super().__init__(value_, next_)
        self.prev_ = None
        self.prev = prev_

    @property
    def prev(self) -> Node:
        return self.prev_

    @prev.setter
    def prev(self, prev_: Optional[Node]):
        self.is_valid(prev_)
        self.prev_ = prev_

    def __repr__(self) -> str:
        first = f"DoubleLinkedNode({self.value}"
        second = f", "
        if self.prev is not None:
            second += f"Node({self.prev.value})"
        else:
            second += f"{None}"
        third = f", "
        if self.prev is not None:
            third += f"Node({self.next.value}))"
        else:
            third += f"{None})"
        return first + second + third

