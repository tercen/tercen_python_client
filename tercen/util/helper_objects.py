import numpy as np
from inspect import ismethod

class ObjectTraverser:
    def __init__(self):
        self.ignoredTypes = [np.number, int, float, str, type]
        self.ignoredKeys = ["__class__", "__delattr__", "__dict__", "__dir__", "__doc__", "__eq__",\
            "__format__", "__ge__", "__hash__", "__getattribute__", "__gt__", "__init__", "__init_subclass__",\
            "__le__", "__lt__", "__reduce__", "__ne__", "__new__", "__reduce_ex__", "__repr__", "__setattr__",\
            "__sizeof__", "__str__", "__subclasshook__", "__weakref__"]
        self.foundList = []
        
    def __ismethod(self, o):
        return str(type(o)) in [ "<class 'method-wrapper'>", "<class 'builtin_function_or_method'>"] or ismethod(o)
    
    def traverse(self, obj, target, targetAttr=None):
        attrs = dir(obj)
        
        for attr in attrs:
            if not attr in self.ignoredKeys:
                attrVal = getattr(obj, attr)
                if not (self.__ismethod(attrVal) or any([isinstance(attrVal, t) for t in self.ignoredTypes])):
                    if isinstance(attrVal, target):
                        if targetAttr is None:
                            self.foundList.append(attrVal)
                        else:
                            self.foundList.append(getattr(attrVal, targetAttr))
                    else: 
                        try:
                            objIterator = iter(attrVal)
                            for o in objIterator:
                                self.traverse(o, target)
                        except TypeError as te:
                            self.traverse(attrVal, target)
                        
        return self.foundList