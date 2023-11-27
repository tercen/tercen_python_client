import unittest
import os

from tercen.model.impl import Task, GitProjectTask, Pair, Document

class TestTercen(unittest.TestCase):

    def meta_test_function(self, obj):
        p1 = Pair({"key":"Key01", "value":"Value01"})
        obj.addMeta("Key01","Value01")


        assert(obj.hasMeta("Key01") == True)
        assert(obj.hasMeta("Key02") == False)

        assert(obj.getMeta("Key01") == "Value01")
        assert(obj.getMeta("Key02") == None)
        assert(obj.getMeta("Key02", defaultValue="") == "")

        p2 = obj.getMetaPair("Key01")
        assert(p1.key == p2.key)
        assert(p1.value == p2.value)


        p3 = Pair({"key":"Key01", "value":"Value01"})
        obj.addMeta("Key01","Value04")
        assert(obj.getMeta("Key01") == "Value04")

        obj.removeMeta("Key01")
        assert(obj.getMeta("Key01") == None)

    def test_inherit_task_base(self):
        task = Task()
        self.meta_test_function(task)


    def test_inherit_task_derived(self):
        task = GitProjectTask()
        self.meta_test_function(task)


    def test_inherit_document(self):
        doc = Document()
        self.meta_test_function(doc)

if __name__ == '__main__':
    unittest.main()
