import unittest
import sys
sys.path.append('/Users/manishak/')
from  Git_Sample import module

class MyModuleTest(unittest.TestCase):

    def test_calc_x(self):
        try:
            assert(module.calc_x(3) == 4)
            print("First test case was Satisfied")
        except:
            print("Failed")
            
    def test_sub(self):
        try:
           assert(module.sub(3) == 1)
           print("Second test case was Satisfied")
        except:
            print("Failed")
    def test_sum(self): 
        try:
           assert(module.sum(3) == 1)
           print("Third test case was Satisfied")
        except:
            print("Failed")
    
    def test_mod(self):
        try:
           assert(module.mod(3) == 1)
           print("Fourth test case was Satisfied")
        except:
            print("Failed")
    
    
             
if __name__ == '__main__':
    unittest.main()