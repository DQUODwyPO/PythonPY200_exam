import unittest

from DoubleLinkedList import DoubleLinkedList

class TestCase(unittest.TestCase):

    def test_delitem(self):
        dll = DoubleLinkedList([1, 2, 3, 4])

        with self.assertRaises(IndexError):
            dll.__delitem__(1)
            dll.__delitem__(-1)
            dll.__delitem__(4)

        with self.assertRaises(TypeError):
            dll.__delitem__("1")
            dll.__delitem__(None)
            dll.__delitem__([1])
            dll.__delitem__({1: 1})

