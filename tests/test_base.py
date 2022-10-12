from python_course_work_projects.base import *


def test_base():
    assert NAME == "python_course_work_projects"
    assert E_OK == True
    assert E_NOT_OK == False
    assert EXAMPLE_DICT == {
        "name": "John",
        "age" : 20,
        "numbers" : [ 34, 21,34, 54,11],
        "params" : {
                "weight" : 80,
                "size"   : 180
            }
        }