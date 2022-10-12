#==============================================================#
#===========================IMPORTS============================#
#==============================================================#

import unittest

from python_course_work_projects.src.functions import (Max_Value_In_Array,
                                                   Print_Array_Of_Numbers)


#==============================================================#
#===========================TESTS==============================#
#==============================================================#

class TestMethods(unittest.TestCase):

    def test_functions(self):
        assert 0 == 0

    def test_Print_Array_Of_Numbers(self):
        assert 0 == 0

    def test_Max_Value_In_Array(self):
        data = [1, 2, 3]
        result = Max_Value_In_Array(data)
        self.assertEqual(result,3)
        self.assertNotEqual(result, 1)

#==============================================================#
#===========================SUITE==============================#
#==============================================================#

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMethods('test_functions'))
    suite.addTest(TestMethods('test_Print_Array_Of_Numbers'))
    suite.addTest(TestMethods('test_Max_Value_In_Array'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())        
        