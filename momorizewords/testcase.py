'''
Created on Oct 14, 2016

@author: linkcare_l10n_rd
'''
import unittest
from document.paper import Word


class Test(unittest.TestCase):
    def setUp(self):
        self.testClass = Word('words.txt')

    def testcase(self):
        for word in self.testClass:
            print word


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testcase']
    unittest.main()