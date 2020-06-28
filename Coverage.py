import unittest
import coverage
from BinaryTree import *

class TestBinaryTree (unittest.TestCase):

    def setUp (self):
        self.tree1 = Tree ()
        self.tree1.add (7)
        self.tree1.add (4)
        self.tree1.add (10)
        self.tree1.add (2)
        self.tree1.add (5)
        self.tree1.add (1)

        self.tree2 = Tree ()
        self.tree2.add (10)
        self.tree2.add (7)
        self.tree2.add (14)
        self.tree2.add (6)
        self.tree2.add (8)
        self.tree2.add (12)
        self.tree2.add (5)
        self.tree2.add (9)
        self.tree2.add (11)
        self.tree2.add (13)
        
    def test_0010_addPost (self):
        self.assertEqual ("1 2 5 4 10 7 ", self.tree1.printTreePostOrder())
        
    def test_0020_addPre (self):
        self.assertEqual ("7 4 2 1 5 10 ", self.tree1.printTreePreOrder())
        
    def test_0030_addIn (self):
        self.assertEqual ("1 2 4 5 7 10 ", self.tree1.printTreeInOrder())

    def test_0040_delete (self):
        self.tree2.delete(5)
        self.tree2.delete(7)
        self.tree2.delete(14)
        self.assertEqual ("6 8 9 10 11 12 13 ", self.tree2.printTreeInOrder())
            
def suite():

   suite = unittest.TestSuite()

   suite.addTests(

       unittest.TestLoader().loadTestsFromTestCase(TestBinaryTree)

   )

   return suite

 

if (__name__ == "__main__"):
    cov = coverage.Coverage()
    cov.start()
    unittest.TextTestRunner(verbosity=2).run(suite())
    cov.stop()
    cov.save()

    cov.html_report()


# .. call your code ..


