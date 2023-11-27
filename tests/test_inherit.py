import unittest
import os

from tercen.model.impl import Task, GitProjectTask, Pair, Document

class TestTercen(unittest.TestCase):
    def test_inherit_task_base(self):
        task = Task()

        p1 = Pair({"key":"Key01", "value":"Value01"})
        task.addMeta(p1)


        assert(task.hasMeta("Key01") == True)
        assert(task.hasMeta("Key02") == False)

        assert(task.getMeta("Key01") == "Value01")
        assert(task.getMeta("Key02") == None)
        assert(task.getMeta("Key02", defaultValue="") == "")

        p2 = task.getMetaPair("Key01")
        assert(p1.key == p2.key)
        assert(p1.value == p2.value)


        p3 = Pair({"key":"Key01", "value":"Value04"})
        task.addMeta(p3)
        assert(task.getMeta("Key01") == "Value04")

        task.removeMeta("Key01")
        assert(task.getMeta("Key01") == None)

    def test_inherit_task_derived(self):
        task = GitProjectTask()

        p1 = Pair({"key":"Key01", "value":"Value01"})
        task.addMeta(p1)


        assert(task.hasMeta("Key01") == True)
        assert(task.hasMeta("Key02") == False)

        assert(task.getMeta("Key01") == "Value01")
        assert(task.getMeta("Key02") == None)
        assert(task.getMeta("Key02", defaultValue="") == "")

        p2 = task.getMetaPair("Key01")
        assert(p1.key == p2.key)
        assert(p1.value == p2.value)


        p3 = Pair({"key":"Key01", "value":"Value04"})
        task.addMeta(p3)
        assert(task.getMeta("Key01") == "Value04")

        task.removeMeta("Key01")
        assert(task.getMeta("Key01") == None)

    def test_inherit_document(self):
        task = Document()

        p1 = Pair({"key":"Key01", "value":"Value01"})
        task.addMeta(p1)


        assert(task.hasMeta("Key01") == True)
        assert(task.hasMeta("Key02") == False)

        assert(task.getMeta("Key01") == "Value01")
        assert(task.getMeta("Key02") == None)
        assert(task.getMeta("Key02", defaultValue="") == "")

        p2 = task.getMetaPair("Key01")
        assert(p1.key == p2.key)
        assert(p1.value == p2.value)


        p3 = Pair({"key":"Key01", "value":"Value04"})
        task.addMeta(p3)
        assert(task.getMeta("Key01") == "Value04")

        task.removeMeta("Key01")
        assert(task.getMeta("Key01") == None)


if __name__ == '__main__':
    unittest.main()
