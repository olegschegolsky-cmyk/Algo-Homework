import unittest
from avl_priority_queue import AVLPriorityQueue

class TestAVLPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.queue = AVLPriorityQueue()

    def test_1(self):
        self.queue.insert("task 1", 10)
        self.queue.insert("task 2", 100)
        self.queue.insert("task 3", 50)

    def test_2(self):
        self.queue.insert("task 1", 10)
        self.queue.insert("task 2", 30)
        self.queue.insert("task 3", 20)
        self.queue.insert("task 4", 50)

    def test_3(self):
        self.queue.insert("task 1", 10)
        self.queue.insert("task 2", 50)
        self.queue.insert("task 3", 100)
        self.queue.insert("task 4", 70)
        self.queue.insert("task 5", 80)

if __name__ == '__main__':
    unittest.main()